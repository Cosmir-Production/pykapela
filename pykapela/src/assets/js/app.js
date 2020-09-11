import $ from 'jquery';
//import 'what-input';

// Foundation JS relies on a global variable. In ES6, all imports are hoisted
// to the top of the file so if we used `import` to import Foundation,
// it would execute earlier than we have assigned the global variable.
// This is why we have to use CommonJS require() here since it doesn't
// have the hoisting behavior.
window.jQuery = $;
window.$ =  $;
require('foundation-sites');

// If you want to pick and choose which modules to include, comment out the above and uncomment
// the line below
//import './lib/foundation-explicit-pieces';

$(document).foundation();

// Hide main menu on mobile:
// var isMedium = Foundation.MediaQuery.atLeast('medium');
// var menuContent = $('.pybazar-menu .accordion-content');
// if (!(isMedium)) { $('.pybazar-menu .accordion').foundation('up', menuContent); }

console.log("It's something!");
