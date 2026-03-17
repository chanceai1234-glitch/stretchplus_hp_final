const fs = require('fs');

function updateHtml(filename) {
    let html = fs.readFileSync(filename, 'utf8');
    
    // Fix container centering for Flow heading
    html = html.replace(
        '<div class="container" style="max-width: 900px; text-align: center; margin-bottom: 30px;">',
        '<div class="container" style="max-width: 900px; text-align: center; margin: 0 auto 30px;">'
    );
    
    // Change badge class to blue
    html = html.replace(/step-badge-orange/g, 'step-badge-blue');

    // Remove 'reveal' class from amenities just in case scroll reveal was hiding it
    html = html.replace(
        '<section id="amenities" class="reveal section-bg-light" style="padding: 60px 0;">',
        '<section id="amenities" class="section-bg-light" style="padding: 60px 0;">'
    );

    fs.writeFileSync(filename, html);
    console.log("Fixed Flow HTML in", filename);
}

updateHtml('index.html');
updateHtml('redesign/index.html');
