# This file provides information and services to the final user.


# LLVM_BUILD_* values available only from LLVM build tree.
set(LLVM_BUILD_BINARY_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build")
set(LLVM_BUILD_LIBRARY_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/./lib")
set(LLVM_BUILD_MAIN_INCLUDE_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/llvm/include")
set(LLVM_BUILD_MAIN_SRC_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/llvm")


set(LLVM_VERSION_MAJOR 12)
set(LLVM_VERSION_MINOR 0)
set(LLVM_VERSION_PATCH 1)
set(LLVM_VERSION_SUFFIX )
set(LLVM_PACKAGE_VERSION 12.0.1)
set(LLVM_PACKAGE_BUGREPORT https://bugs.llvm.org/)

set(LLVM_BUILD_TYPE Release)

set(LLVM_USE_CRT_DEBUG )
set(LLVM_USE_CRT_MINSIZEREL )
set(LLVM_USE_CRT_RELEASE )
set(LLVM_USE_CRT_RELWITHDEBINFO )

set(LLVM_USE_SPLIT_DWARF OFF)

set(LLVM_COMMON_DEPENDS )

set(LLVM_AVAILABLE_LIBS LLVMDemangle;LLVMSupport;LLVMTableGen;LLVMCore;LLVMFuzzMutate;LLVMFileCheck;LLVMInterfaceStub;LLVMIRReader;LLVMCodeGen;LLVMSelectionDAG;LLVMAsmPrinter;LLVMMIRParser;LLVMGlobalISel;LLVMBinaryFormat;LLVMBitReader;LLVMBitWriter;LLVMBitstreamReader;LLVMDWARFLinker;LLVMExtensions;LLVMFrontendOpenACC;LLVMFrontendOpenMP;LLVMTransformUtils;LLVMInstrumentation;LLVMAggressiveInstCombine;LLVMInstCombine;LLVMScalarOpts;LLVMipo;LLVMVectorize;LLVMHelloNew;LLVMObjCARCOpts;LLVMCoroutines;LLVMCFGuard;LLVMObfuscation;LLVMLinker;LLVMAnalysis;LLVMLTO;LLVMMC;LLVMMCParser;LLVMMCDisassembler;LLVMMCA;LLVMObject;LLVMObjectYAML;LLVMOption;LLVMRemarks;LLVMDebugInfoDWARF;LLVMDebugInfoGSYM;LLVMDebugInfoMSF;LLVMDebugInfoCodeView;LLVMDebugInfoPDB;LLVMSymbolize;LLVMExecutionEngine;LLVMInterpreter;LLVMJITLink;LLVMMCJIT;LLVMOrcJIT;LLVMOrcShared;LLVMOrcTargetProcess;LLVMRuntimeDyld;LLVMTarget;LLVMX86CodeGen;LLVMX86AsmParser;LLVMX86Disassembler;LLVMX86Desc;LLVMX86Info;LLVMAsmParser;LLVMLineEditor;LLVMProfileData;LLVMCoverage;LLVMPasses;LLVMTextAPI;LLVMDlltoolDriver;LLVMLibDriver;LLVMXRay;LLVMWindowsManifest;LTO;Remarks)



set(LLVM_DYLIB_COMPONENTS all)

set(LLVM_ALL_TARGETS AArch64;AMDGPU;ARM;AVR;BPF;Hexagon;Lanai;Mips;MSP430;NVPTX;PowerPC;RISCV;Sparc;SystemZ;WebAssembly;X86;XCore)

set(LLVM_TARGETS_TO_BUILD X86)

set(LLVM_TARGETS_WITH_JIT X86;PowerPC;AArch64;ARM;Mips;SystemZ)


set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDemangle )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMSupport )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMTableGen )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMCore )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMFuzzMutate )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMFileCheck )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMInterfaceStub )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMIRReader )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMCodeGen )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMSelectionDAG )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMAsmPrinter )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMMIRParser )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMGlobalISel )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMBinaryFormat )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMBitReader )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMBitWriter )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMBitstreamReader )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDWARFLinker )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMExtensions )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMFrontendOpenACC )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMFrontendOpenMP )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMTransformUtils )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMInstrumentation )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMAggressiveInstCombine )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMInstCombine )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMScalarOpts )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMipo )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMVectorize )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMHelloNew )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMObjCARCOpts )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMCoroutines )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMCFGuard )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMObfuscation )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMLinker )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMAnalysis )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMLTO )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMMC )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMMCParser )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMMCDisassembler )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMMCA )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMObject )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMObjectYAML )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMOption )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMRemarks )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDebugInfoDWARF )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDebugInfoGSYM )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDebugInfoMSF )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDebugInfoCodeView )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDebugInfoPDB )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMSymbolize )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMExecutionEngine )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMInterpreter )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMJITLink )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMMCJIT )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMOrcJIT )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMOrcShared )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMOrcTargetProcess )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMRuntimeDyld )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMTarget )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMX86CodeGen )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMX86AsmParser )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMX86Disassembler )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMX86Desc )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMX86Info )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMAsmParser )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMLineEditor )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMProfileData )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMCoverage )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMPasses )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMTextAPI )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMDlltoolDriver )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMLibDriver )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMXRay )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LLVMWindowsManifest )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_LTO )
set_property(GLOBAL PROPERTY LLVMBUILD_LIB_DEPS_Remarks )

set(TARGET_TRIPLE "x86_64-unknown-linux-gnu")

set(LLVM_ABI_BREAKING_CHECKS WITH_ASSERTS)

set(LLVM_ENABLE_WARNINGS ON)

set(LLVM_ENABLE_EXPENSIVE_CHECKS OFF)

set(LLVM_ENABLE_ASSERTIONS OFF)

set(LLVM_ENABLE_EH OFF)

set(LLVM_ENABLE_RTTI OFF)

set(LLVM_ENABLE_TERMINFO 1)

set(LLVM_ENABLE_THREADS ON)

set(LLVM_ENABLE_UNWIND_TABLES ON)

set(LLVM_ENABLE_ZLIB 1)
if(LLVM_ENABLE_ZLIB)
  find_package(ZLIB)
endif()

set(LLVM_ENABLE_LIBXML2 1)
if(LLVM_ENABLE_LIBXML2)
  find_package(LibXml2)
endif()

set(LLVM_WITH_Z3 )

set(LLVM_ENABLE_DIA_SDK 0)

set(LLVM_NATIVE_ARCH X86)

set(LLVM_ENABLE_PIC ON)

set(LLVM_BUILD_32_BITS OFF)

if (NOT "-lpthread" STREQUAL "")
  set(LLVM_PTHREAD_LIB "-lpthread")
endif()

set(LLVM_ENABLE_PLUGINS ON)
set(LLVM_EXPORT_SYMBOLS_FOR_PLUGINS OFF)
set(LLVM_PLUGIN_EXT .so)

set(LLVM_ON_UNIX 1)

set(LLVM_LIBDIR_SUFFIX )

set(LLVM_INCLUDE_DIRS "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/llvm/include;/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/include")
set(LLVM_LIBRARY_DIRS "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/./lib")

set(LLVM_APPEND_VC_REV "ON")

# These variables are duplicated for install tree but they have different
# values for build tree.  LLVM_INCLUDE_DIRS contains both source
# and generated include directories while the following variables have
# them split.
set(LLVM_INCLUDE_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/include")
set(LLVM_MAIN_INCLUDE_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/llvm/include")
set(LLVM_LIBRARY_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/./lib")

set(LLVM_DEFINITIONS "-D_GNU_SOURCE -D__STDC_CONSTANT_MACROS -D__STDC_FORMAT_MACROS -D__STDC_LIMIT_MACROS")
set(LLVM_CMAKE_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/llvm/cmake/modules")
set(LLVM_BINARY_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build")
set(LLVM_TOOLS_BINARY_DIR "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/./bin")
set(LLVM_TOOLS_INSTALL_DIR "bin")
set(LLVM_HAVE_OPT_VIEWER_MODULES 0)
set(LLVM_CONFIGURATION_TYPES )
set(LLVM_ENABLE_SHARED_LIBS On)

set(LLVM_DEFAULT_EXTERNAL_LIT "/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/./bin/llvm-lit")
set(LLVM_LIT_ARGS "-sv")

if(NOT TARGET LLVMSupport)
  set(LLVM_EXPORTED_TARGETS "LLVMDemangle;LLVMSupport;LLVMTableGen;llvm-tblgen;LLVMCore;LLVMFuzzMutate;LLVMFileCheck;LLVMInterfaceStub;LLVMIRReader;LLVMCodeGen;LLVMSelectionDAG;LLVMAsmPrinter;LLVMMIRParser;LLVMGlobalISel;LLVMBinaryFormat;LLVMBitReader;LLVMBitWriter;LLVMBitstreamReader;LLVMDWARFLinker;LLVMExtensions;LLVMFrontendOpenACC;LLVMFrontendOpenMP;LLVMTransformUtils;LLVMInstrumentation;LLVMAggressiveInstCombine;LLVMInstCombine;LLVMScalarOpts;LLVMipo;LLVMVectorize;LLVMHelloNew;LLVMObjCARCOpts;LLVMCoroutines;LLVMCFGuard;LLVMObfuscation;LLVMLinker;LLVMAnalysis;LLVMLTO;LLVMMC;LLVMMCParser;LLVMMCDisassembler;LLVMMCA;LLVMObject;LLVMObjectYAML;LLVMOption;LLVMRemarks;LLVMDebugInfoDWARF;LLVMDebugInfoGSYM;LLVMDebugInfoMSF;LLVMDebugInfoCodeView;LLVMDebugInfoPDB;LLVMSymbolize;LLVMExecutionEngine;LLVMInterpreter;LLVMJITLink;LLVMMCJIT;LLVMOrcJIT;LLVMOrcShared;LLVMOrcTargetProcess;LLVMRuntimeDyld;LLVMTarget;LLVMX86CodeGen;LLVMX86AsmParser;LLVMX86Disassembler;LLVMX86Desc;LLVMX86Info;LLVMAsmParser;LLVMLineEditor;LLVMProfileData;LLVMCoverage;LLVMPasses;LLVMTextAPI;LLVMDlltoolDriver;LLVMLibDriver;LLVMXRay;LLVMWindowsManifest;LTO;llvm-ar;llvm-config;llvm-lto;llvm-profdata;clang-tblgen;bugpoint;dsymutil;llc;lli;llvm-as;llvm-bcanalyzer;llvm-c-test;llvm-cat;llvm-cfi-verify;llvm-cov;llvm-cvtres;llvm-cxxdump;llvm-cxxfilt;llvm-cxxmap;llvm-diff;llvm-dis;llvm-dwarfdump;llvm-dwp;llvm-elfabi;llvm-exegesis;llvm-extract;llvm-gsymutil;llvm-ifs;llvm-jitlink;llvm-libtool-darwin;llvm-link;llvm-lipo;llvm-lto2;llvm-mc;llvm-mca;llvm-ml;llvm-modextract;llvm-mt;llvm-nm;llvm-objcopy;llvm-objdump;llvm-opt-report;llvm-pdbutil;llvm-profgen;llvm-rc;llvm-readobj;llvm-reduce;llvm-rtdyld;llvm-size;llvm-split;llvm-stress;llvm-strings;llvm-symbolizer;llvm-undname;llvm-xray;opt;Remarks;sancov;sanstats;split-file;verify-uselistorder;LLVMHello;LLVMTestingSupport;FileCheck;llvm-PerfectShuffle;count;not;yaml-bench;SampleAnalyzerPlugin;CheckerDependencyHandlingAnalyzerPlugin;CheckerOptionHandlingAnalyzerPlugin;BugpointPasses;lli-child-target;llvm-jitlink-executor;obj2yaml;yaml2obj;Bye;TestPlugin;gtest;gtest_main")
  include("/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/lib/cmake/llvm/LLVMExports.cmake")
  include("/home/bailin/project/crossctf22-challs/challenges/re/nahhhh/Pluto-Obfuscator/build/lib/cmake/llvm/LLVMBuildTreeOnlyTargets.cmake")
endif()

# By creating intrinsics_gen, omp_gen and acc_gen here, subprojects that depend
# on LLVM's tablegen-generated headers can always depend on this target whether
# building in-tree with LLVM or not.
if(NOT TARGET intrinsics_gen)
  add_custom_target(intrinsics_gen)
endif()
if(NOT TARGET omp_gen)
  add_custom_target(omp_gen)
endif()
if(NOT TARGET acc_gen)
  add_custom_target(acc_gen)
endif()

set_property(GLOBAL PROPERTY LLVM_TARGETS_CONFIGURED On)
include(${LLVM_CMAKE_DIR}/LLVM-Config.cmake)
