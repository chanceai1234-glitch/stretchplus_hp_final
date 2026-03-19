<!-- Pre-Footer CTA -->
    <div class="bottom-cta-banner">
        <div class="container">
            <h3>まずは1回、体感してみてください。</h3>
            <p style="color: #fff; font-size: 1.1rem; margin-bottom: 25px; font-weight: bold; text-shadow: 1px 1px 3px rgba(0,0,0,0.2);">初回限定価格 60分 3,980円（税込）</p>
            <div style="display: flex; gap: 30px; justify-content: center; flex-wrap: wrap;">
                <!-- Group 1: WEB & Hotpepper -->
                <div style="display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%; max-width: 350px;">
                    <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn-web-outline pulse-btn cta-universal-btn" target="_blank"><i class="far fa-file-alt" style="margin-right:8px;"></i> WEBで予約する</a>
                    <a href="https://beauty.hotpepper.jp/kr/slnH000671756/" class="btn btn-hotpepper cta-universal-btn btn-aux-red" target="_blank">Hot Pepper Beautyで予約</a>
                </div>

                <!-- Group 2: LINE & Rakuten -->
                <div style="display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%; max-width: 350px;">
                    <a href="https://lin.ee/rboKm7N" class="btn-line-outline pulse-btn cta-universal-btn" target="_blank"><i class="fab fa-line" style="margin-right:8px;"></i> LINEで相談する</a>
                    <a href="https://beauty.rakuten.co.jp/s3000052366/" class="btn btn-rakuten cta-universal-btn btn-aux-red" target="_blank">楽天ビューティーで予約</a>
                </div>
            </div>
        </div>
    </div>

    <footer id="footer">
        <div class="footer-content">
            <!-- 左カラム: ロゴ・住所・電話 -->
            <div class="footer-left">
                <img src="<?php echo get_template_directory_uri(); ?>/image_final/common_logo.png" alt="ストレッチplus ロゴ" width="200" class="footer-logo-img">
                <div class="footer-nap">
                    <p>〒103-0025 東京都中央区日本橋茅場町<br>2-13-14 ブイワンビル2F</p>
                    <p class="footer-tel">TEL: 080-7137-9086</p>
                </div>
            </div>
            
            <!-- 中央カラム: ナビゲーション -->
            <div class="footer-nav">
                <ul>
                    <li><a href="#about">パーソナルストレッチとは</a></li>
                    <li><a href="#worries">こんなお悩みありませんか？</a></li>
                    <li><a href="#reviews">お客様の声</a></li>
                    <li><a href="#amenities">豊富な設備・アメニティ</a></li>
                    <li><a href="#flow">ご利用の流れ</a></li>
                    <li><a href="#policy">私たちが大切にしていること</a></li>
                    <li><a href="#trainers">トレーナー紹介</a></li>
                    <li><a href="#menu">メニュー/料金</a></li>
                    <li><a href="#info">店舗情報・アクセス</a></li>
                    <li><a href="#faq">よくあるご質問</a></li>
                </ul>
            </div>
            
            <!-- 右カラム: SNS -->
            <div class="footer-right">
                <div class="footer-sns-wrap">
                    <span class="sns-label">Follow us</span>
                    <div class="footer-sns">
                        <a href="https://www.instagram.com/stretchplus/" target="_blank">
                            <img src="<?php echo get_template_directory_uri(); ?>/image_final/icon_instagram.svg" alt="Instagram">
                        </a>
                        <a href="https://x.com/stretch_plus_?s=11&t=QlOrwZ5pbRCsq3muCuRckw" target="_blank">
                            <img src="<?php echo get_template_directory_uri(); ?>/image_final/icon_x.svg" alt="X (Twitter)">
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <ul>
                <li><a href="<?php echo get_template_directory_uri(); ?>/privacy-policy.html">プライバシーポリシー</a></li>
                <li><a href="<?php echo get_template_directory_uri(); ?>/terms.html">利用規約</a></li>
                <li><a href="<?php echo get_template_directory_uri(); ?>/cookie-policy.html">Cookie方針</a></li>
            </ul>
            <p>&copy; 2026 ストレッチplus</p>
        </div>
    </footer>

    <!-- Floating QR Code (PC Only) -->
    <div id="floating-qr">
        <p class="qr-title">LINEで相談</p>
        <img src="<?php echo get_template_directory_uri(); ?>/image_final/common_qr_line.png" alt="LINE友達追加QRコード"
            style="border: 1px solid #E2E8F0; border-radius: 8px; padding: 5px; background: #fff;">
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.2, rootMargin: "0px 0px -50px 0px" });

            // スクロールアニメーション (全セクション & フローカード)
            document.querySelectorAll('.reveal, .flow-card').forEach(el => {
                observer.observe(el);
            });

            // ヘッダーのスクロール変化
            const header = document.getElementById('header');
            window.addEventListener('scroll', () => {
                if (window.scrollY > 50) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
            });

            // Review Slider Logic
            const reviewGrid = document.getElementById('review-grid');
            const prevReviewBtn = document.getElementById('review-prev');
            const nextReviewBtn = document.getElementById('review-next');
            const reviewProgress = document.getElementById('review-progress');
            if (reviewGrid && prevReviewBtn && nextReviewBtn) {
                let currentSlide = 0;
                // Determine items per view based on window width
                const getItemsPerView = () => window.innerWidth <= 600 ? 1 : (window.innerWidth <= 900 ? 2 : 3);
                
                const updateSliderPosition = () => {
                    const cards = reviewGrid.querySelectorAll('.review-card');
                    if (cards.length === 0) return;
                    const itemsPerView = getItemsPerView();
                    const maxSlide = Math.max(0, cards.length - itemsPerView);
                    if (currentSlide > maxSlide) currentSlide = maxSlide;
                    if (currentSlide < 0) currentSlide = 0;
                    
                    const cardWidth = cards[0].offsetWidth;
                    const gap = 30; // 30px gap
                    const offset = currentSlide * (cardWidth + gap);
                    reviewGrid.style.transform = `translateX(-${offset}px)`;

                    // Update Progress Bar
                    if (reviewProgress) {
                        if (maxSlide === 0) {
                            reviewProgress.style.width = '100%';
                            reviewProgress.style.transform = 'translateX(0)';
                        } else {
                            // Calculate percentage based on current index vs max index
                            const percentage = (currentSlide / maxSlide) * 100;
                            // Width is proportion of visible items to total items
                            const widthPercent = (itemsPerView / cards.length) * 100;
                            reviewProgress.style.width = `${widthPercent}%`;
                            // Translate by remaining percentage
                            const translatePercent = percentage * (100 - widthPercent) / 100;
                            reviewProgress.style.transform = `translateX(${percentage * (100 - widthPercent) / 100}%)`;
                            // Quick alternative for absolute positioning of progress bar:
                            reviewProgress.style.left = `${translatePercent}%`;
                            reviewProgress.style.transform = 'none';
                        }
                    }
                };

                prevReviewBtn.addEventListener('click', () => {
                    const itemsPerView = getItemsPerView();
                    if (currentSlide > 0) {
                        currentSlide = Math.max(0, currentSlide - itemsPerView);
                        updateSliderPosition();
                    }
                });

                nextReviewBtn.addEventListener('click', () => {
                    const cards = reviewGrid.querySelectorAll('.review-card');
                    const itemsPerView = getItemsPerView();
                    const maxSlide = Math.max(0, cards.length - itemsPerView);
                    if (currentSlide < maxSlide) {
                        currentSlide = Math.min(maxSlide, currentSlide + itemsPerView);
                        updateSliderPosition();
                    }
                });

                window.addEventListener('resize', updateSliderPosition);
                // Call initially
                updateSliderPosition();
            }
        });
    
    // Store Info Slideshow
    const slides = document.querySelectorAll('#shopSlideshow .slide');
    if(slides.length > 0) {
        let currentSlide = 0;
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 4000); // Change image every 4 seconds
    }
</script>
<?php wp_footer(); ?>
</body>


</html>
