const fs = require('fs');
let css = fs.readFileSync('style.css', 'utf8');

// Increase padding to push buttons out
css = css.replace('padding: 20px 40px;', 'padding: 20px 70px;');

// Move prev-btn left to 5px (inside the 70px padding, gives 65px for the 60px button, so 5px gap from edge)
// Adjust vertical centering for buttons against the review cards (cards are the only flex items growing, but let's make sure it's top: 50%)
css = css.replace('.prev-btn {\n    left: 0;\n}', '.prev-btn {\n    left: 5px;\n}');
css = css.replace('.next-btn {\n    right: 0;\n}', '.next-btn {\n    right: 5px;\n}');

fs.writeFileSync('style.css', css);

let cssRedesign = fs.readFileSync('redesign/style.css', 'utf8');
cssRedesign = cssRedesign.replace('padding: 20px 40px;', 'padding: 20px 70px;');
cssRedesign = cssRedesign.replace('.prev-btn {\n    left: 0;\n}', '.prev-btn {\n    left: 5px;\n}');
cssRedesign = cssRedesign.replace('.next-btn {\n    right: 0;\n}', '.next-btn {\n    right: 5px;\n}');
fs.writeFileSync('redesign/style.css', cssRedesign);

console.log("Updated CSS padding for buttons");
