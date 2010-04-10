// add tools to code highlighting blocks
(function () {

var OPTIONS = { 'duration': 300 };

// insert the toolbox in every code block
u('.codehilite').prepend('div.tools');

// apply a nice effect to the toolbox
u('.codehilite').on('mouseenter,mouseleave', function (e) {
    u(this).first().anim({ 'opacity': +(e.type == 'mouseenter') * 1 }, OPTIONS) });

// copy code blocks to textareas
for (var i = -1, blocks = u('.codehilite'), block; blocks[++i];) {
    block = u(blocks[i]);
    block.append('textarea', block.text()).hide() }

// adds button to show/hide the created textareas
u('.codehilite .tools')
    .append('button', 'toggle plain code').on('click', function () {
        var block = u(this).up(2);
        block.first('textarea').css(block.first('pre').size()).toggle().prev().toggle() });

// opacity effect for buttons
u('.codehilite .tools').css({ 'opacity': 0 })
    .children().css({ 'opacity': .5 }).hover({ 'opacity': 1 }, OPTIONS)

})()
