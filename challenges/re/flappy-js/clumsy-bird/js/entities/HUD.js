game.HUD = game.HUD || {};

game.HUD.Container = me.Container.extend({
    init: function() {
        this._super(me.Container, 'init');
        // persistent across level change
        this.isPersistent = true;

        // non collidable
        this.collidable = false;

        // make sure our object is always draw first
        this.z = Infinity;

        // give a name
        this.name = "HUD";

        // add our child score object at the top left corner
        this.addChild(new game.HUD.ScoreItem(5, 5));
    }
});


game.HUD.ScoreItem = me.Renderable.extend({
    init: function(x, y) {
        this._super(me.Renderable, "init", [x, y, 10, 10]);

        // local copy of the global score
        this.stepsFont = new me.Font('gamefont', 80, '#000', 'center');

        // make sure we use screen coordinates
        this.floating = true;

        this.flag = "";
    },

    draw: function (renderer) {
        if (game.data.start && me.state.isCurrent(me.state.PLAY)) {
            this.stepsFont.draw(renderer, game.data.steps, me.game.viewport.width/2, 10);
            if (game.data.steps >= 31337) {
                if (this.flag.length == 0) this.flag = genFlag();
                this.flagFont = new me.Font('roboto', 35, '#000', 'center');
                this.flagFont.draw(renderer, "greyctf{" + this.flag + "}", me.game.viewport.width/2, 110);
            }
        }
    }

});

var BackgroundLayer = me.ImageLayer.extend({
    init: function(image, z, speed) {
        var settings = {};
        settings.name = image;
        settings.width = 900;
        settings.height = 600;
        settings.image = image;
        settings.z = z;
        settings.ratio = 1;
        // call parent constructor
        this._super(me.ImageLayer, 'init', [0, 0, settings]);
    },

    update: function() {
        if (me.input.isKeyPressed('mute')) {
            game.data.muted = !game.data.muted;
            if (game.data.muted){
                me.audio.disable();
            }else{
                me.audio.enable();
            }
        }
        return true;
    }
});

var genFlag = function() {
    var v = "AzhkZTRlYB0GDT0NAhItAQw4LR4DEzkABjkbAwM5DywDOCFlAhIfEgY5DwMDZgQiAxETNDZkGyYPEzEbAz4lDAIDDz4HZWAmAjsfPAc5Dw0DPx87MDkxAg8RBz4YEQMsAQMDAjQSAyQEAT5o";
    v = atob(v);
    var v2 = "";
    for (var i in v) v2 += String.fromCharCode(v.charCodeAt(i) ^ 0x55)
    v2 = v2.substring(0, v2.indexOf("=") + 1);
    v2 = atob(v2);
    v2 = atob(v2);
    v2 = atob(v2);
    v2 = atob(v2);
    v2 = atob(v2);
    v2 = atob(v2);
    return v2;
};
