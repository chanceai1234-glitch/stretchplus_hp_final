<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="茅場町駅徒歩1分。完全個室で人目を気にせず施術が受けられる、パーソナルストレッチ専門店のストレッチplusです。体が不調になる前に整えて、元気が続く毎日へ。">
    <title>ストレッチplus | 茅場町駅徒歩1分のパーソナルストレッチ専門店</title>
    <!-- Google Fonts (Dual-font strategy) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="<?php echo get_template_directory_uri(); ?>/style.css">
    <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
    <?php wp_body_open(); ?>

    <!-- Section 0: ヘッダー -->
    <header id="header">
        <div class="header-logo">
            <a href="#">
                <img src="<?php echo get_template_directory_uri(); ?>/image_final/common_logo.png" alt="ストレッチplus ロゴ" width="200">
            </a>
        </div>
        
        <!-- Hamburger Button (Mobile Only) -->
        <button class="hamburger-btn sp-only" id="hamburger-btn" aria-label="Menu">
            <span></span>
            <span></span>
            <span></span>
        </button>

        <nav class="header-nav" id="header-nav">
            <ul>
                <li><a href="#about">パーソナルストレッチとは</a></li>
                <li><a href="#worries">よくあるお悩み</a></li>
                <li><a href="#reviews">お客様の声</a></li>
                <li><a href="#flow">ご利用の流れ</a></li>
                <li><a href="#menu">メニュー/料金</a></li>
                <li><a href="#info">店舗情報</a></li>
                <li><a href="#access">アクセス</a></li>
            </ul>
        </nav>
        <div class="header-actions">
            <a href="https://yui.kanzashi.com/l/stretch-plus/kirei" class="btn btn-web" target="_blank">WEBで予約する</a>
            <a href="https://lin.ee/rboKm7N" class="btn btn-line" target="_blank">LINEで相談する</a>
        </div>
    </header>