<?php
/**
 * STRETCH+ functions and definitions
 */

function stretchplus_enqueue_assets() {
    // Enqueue the main stylesheet with dynamic cache busting based on file modification time
    $theme_version = filemtime(get_stylesheet_directory() . '/style.css');
    wp_enqueue_style('stretchplus-style', get_stylesheet_uri(), array(), $theme_version);

    // Remove WordPress default blocks CSS as we use entirely custom CSS
    wp_dequeue_style('wp-block-library');
    wp_dequeue_style('wp-block-library-theme');
    wp_dequeue_style('wc-blocks-style'); // If WooCommerce exists
}
add_action('wp_enqueue_scripts', 'stretchplus_enqueue_assets');

function stretchplus_theme_setup() {
    // Add default posts and comments RSS feed links to head.
    add_theme_support('automatic-feed-links');

    // Let WordPress manage the document title.
    // add_theme_support('title-tag'); // DISABLED: We use hardcoded SEO title in header.php to strictly enforce Japanese branding

    // Enable support for Post Thumbnails on posts and pages.
    add_theme_support('post-thumbnails');

    // Register Navigation Menus
    register_nav_menus(array(
        'menu-1' => esc_html__('Primary', 'stretchplus'),
    ));
}
add_action('after_setup_theme', 'stretchplus_theme_setup');

// Add SVG support to media uploader
function cc_mime_types($mimes) {
    if (current_user_can('manage_options')) {
        $mimes['svg'] = 'image/svg+xml';
    }
    return $mimes;
}
add_filter('upload_mimes', 'cc_mime_types');

// Google Tag Manager Event Tracking for CTAs
function stretchplus_add_gtm_tracking() {
    ?>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var pushDataLayer = function(type) {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'click_cta',
                'button_type': type
            });
        };
        // WEB Reservation
        document.querySelectorAll('.btn-web, a[href*="kanzashi.com"]').forEach(function(btn) {
            btn.addEventListener('click', function() { pushDataLayer('web_reservation'); });
        });
        // LINE Contact
        document.querySelectorAll('.btn-line, a[href*="lin.ee"]').forEach(function(btn) {
            btn.addEventListener('click', function() { pushDataLayer('line_contact'); });
        });
        // HotPepper
        document.querySelectorAll('.btn-hotpepper, a[href*="hotpepper.jp"]').forEach(function(btn) {
            btn.addEventListener('click', function() { pushDataLayer('hotpepper'); });
        });
        // Rakuten
        document.querySelectorAll('.btn-rakuten, a[href*="beauty.rakuten.co.jp"]').forEach(function(btn) {
            btn.addEventListener('click', function() { pushDataLayer('rakuten'); });
        });
    });
    </script>
    <?php
}
add_action('wp_footer', 'stretchplus_add_gtm_tracking', 100);
