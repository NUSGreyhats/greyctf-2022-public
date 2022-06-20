console.log("Script loaded successfully ");
Java.perform(function x() { //Silently fails without the sleep from the python code
    console.log("Inside java perform function");
    //get a wrapper for our class
    var Engine = Java.use("com.snatik.matches.engine.Engine");
    console.log(Engine)
    console.log(Engine.onEvent.overloads)

    // https://gist.github.com/FrankSpierings/6e2608e22121b1aeaaa4588f13387dde?permalink_comment_id=4063154#gistcomment-4063154
    // for (var m of Engine.onEvent.overloads) {
    //     console.log(m.argumentTypes[0].className)
    // }

    // console.log(Engine.onEvent.overload("com.snatik.matches.events.ui.FlipCardEvent"))

    //replace the original implmenetation of the function `fun` with our custom function
    Engine.onEvent.overload("com.snatik.matches.events.ui.FlipCardEvent").implementation = function (e) {
        //print the original arguments
        console.log("flip card event called");
        console.log(this)
        // console.log(this.mPlayingGame.value)
        // console.log(this.mPlayingGame.value.boardConfiguration.value)
        console.log("Current difficulty is")
        console.log(this.mPlayingGame.value.boardConfiguration.value.difficulty.value)
        this.mPlayingGame.value.boardConfiguration.value.difficulty.value = 6

        //call the original implementation of `onEvent`
        this.onEvent(e)
    }
});