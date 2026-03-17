const fs = require('fs');
let html = fs.readFileSync('redesign/index.html', 'utf8');

const replacement = `    <!-- Section 6: 豊富な設備・アメニティ -->
    <section id="amenities" class="reveal section-bg-light" style="padding: 60px 0;">
        <div class="amenities-container fade-in">
            <h2>豊富な設備・アメニティ</h2>
            <div class="amenities-grid">
                <!-- Amenity 1 -->
                <div class="amenity-card">
                    <div class="amenity-img-wrapper">
                        <img src="./images/hero_private_room.png" alt="完全個室">
                    </div>
                    <div class="amenity-content">
                        <h3><span class="amenity-number">01</span>完全個室</h3>
                        <p>プライベートな空間で、他人の目を気にせず、リラックスした状態で施術に臨むことができます。</p>
                    </div>
                </div>
                <!-- Amenity 2 -->
                <div class="amenity-card">
                    <div class="amenity-img-wrapper">
                        <img src="./images/clinic_room_bed.jpg" alt="温熱機能付きベッド" onerror="this.src='./images/clinic_room.jpg'">
                    </div>
                    <div class="amenity-content">
                        <h3><span class="amenity-number">02</span>温熱機能付きベッド</h3>
                        <p>リラックス効果を高めます。また、冷え性の方にもオススメです。<br>※お客様に合わせて温度を調節可能。</p>
                    </div>
                </div>
                <!-- Amenity 3 -->
                <div class="amenity-card">
                    <div class="amenity-img-wrapper">
                        <img src="./images/about_intro.jpg" alt="シャワー＆施術着など">
                    </div>
                    <div class="amenity-content">
                        <h3><span class="amenity-number">03</span>シャワー＆施術着など</h3>
                        <p>シャワーはいつでもお気軽にご利用いただけます。<br>施術着や靴下、タオルなどご用意しておりますので、手ぶらでお越しください。</p>
                    </div>
                </div>
            </div>
        </div>
    </section>`;

const startIdx = html.indexOf('    <!-- Section 6: 豊富な設備・アメニティ -->');
const endIdx = html.indexOf('    <!-- Section 7: 施術の流れ -->');

if (startIdx !== -1 && endIdx !== -1) {
    html = html.substring(0, startIdx) + replacement + '\n\n' + html.substring(endIdx);
    fs.writeFileSync('redesign/index.html', html);
    console.log("Updated redesign/index.html amenities.");
} else {
    console.log("Could not find amenities section in redesign/index.html");
}

let htmlMain = fs.readFileSync('index.html', 'utf8');
const startIdxMain = htmlMain.indexOf('    <!-- Section 6: 豊富な設備・アメニティ -->');
const endIdxMain = htmlMain.indexOf('    <!-- Section 7: 施術の流れ -->');
if (startIdxMain !== -1 && endIdxMain !== -1) {
    htmlMain = htmlMain.substring(0, startIdxMain) + replacement + '\n\n' + htmlMain.substring(endIdxMain);
    fs.writeFileSync('index.html', htmlMain);
    console.log("Updated index.html amenities.");
}

