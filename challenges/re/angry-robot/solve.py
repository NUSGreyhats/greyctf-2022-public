import angr 
import sys

import claripy

input_size = 0
expect1 = b""
expect2 = b""

def get_main_addr(cfg):
    main_addr = list(filter(lambda f: cfg.kb.functions[f].name=="main", cfg.kb.functions))[0]

    if not main_addr:
        print ("failed to find main address, key in manually")
        
    return main_addr


class FgetsSim(angr.sim_procedure.SimProcedure):
    def run(self, buf, size, fd):
        global input_size
        input_size = self.state.solver.eval(size, int)-1
        return 0;
    
class LoopSim(angr.sim_procedure.SimProcedure):
    def run(self):
        state = self.state
        
        # align input size to 64 bit addressing
        aligned_input_size =(input_size + 7) & ~7
        offset = aligned_input_size*2+0x10
        expect1_addr = state.regs.rbp-(offset)
        expect2_addr = expect1_addr+aligned_input_size
        
        
        global expect1
        global expect2

        expect1 = state.memory.load(expect1_addr, input_size)
        expect1 = state.solver.eval(expect1, cast_to=bytes)
        expect2 = state.memory.load(expect2_addr, input_size)
        expect2 = state.solver.eval(expect2, cast_to=bytes)
        
        

def main():
    # initialise stuff
    path = sys.argv[1]
    project = angr.Project(path, load_options={'auto_load_libs': False})
    
        
    # getting the scramble function
    cfg = project.analyses.CFGFast()  # type: ignore   
    main_func = cfg.kb.functions[get_main_addr(cfg)]
    
    t = list(main_func.get_call_sites())[1]
    check_addr = main_func.get_call_target(t)
    check_func = cfg.kb.functions[check_addr]
    
    
    loopblock = list(check_func.get_call_sites())[0] # the loop
    
    scramble_addr = check_func.get_call_target(loopblock)
    
    f = project.factory.callable(scramble_addr, prototype="char x(char, int)")
    
    # getting input size
    
    project.hook_symbol("fgets", FgetsSim())

    # getting expected values
    
    project.hook(loopblock-2, LoopSim())
    
    simgr = project.factory.simgr()
    simgr.explore(find=loopblock) # can terminate here
    
    global input_size
    global expect1
    global expect2
    
    print (input_size, expect1, expect2)
    
    user_input = [claripy.BVS("c{}".format(i), 8) for i in range(input_size)]
    ans = bytearray()
    i = 0
    for u,e1,e2 in zip(user_input, expect1, expect2):
        solver = claripy.solvers.Solver()
        solver.add(f(u, i) == claripy.BVV(e1, 8))
        solver.add(f(u, e1) == claripy.BVV(e2, 8))
        solver.add(claripy.And(u>=0x20, u<127))

        ans.append(solver.eval(u, 8)[0])
        i += 1
    
    open("answers/{}.txt".format(sys.argv[1]), "wb").write(ans)
    
    return 0
    

def poc():
    path = sys.argv[1]
    project = angr.Project(path)
    
    f = project.factory.callable(0x0401176, prototype="char x(char, int)")

    user_input = [claripy.BVS("c{}".format(i), 8) for i in range(30)]
    
    expect1 = "WosrtEo<iYDove9]P;cVa2If8rAd5T"
    expect2 = "GTbmsIOOuZZ3i=`2^K>vl;SL^t=@f`"
    
    ans = []
    i = 0
    for u,e1,e2 in zip(user_input, expect1, expect2):
        solver = claripy.solvers.Solver()
        solver.add(f(u, i) == claripy.BVV(ord(e1), 8))
        solver.add(f(u, ord(e1)) == claripy.BVV(ord(e2), 8))

        ans.append(chr(solver.eval(u, 8)[0]))
        i += 1
    
    print ("".join(ans))

if __name__ == "__main__":
    main()
