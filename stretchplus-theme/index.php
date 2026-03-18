<?php
/**
 * The main template file
 *
 * This is the most generic template file in a WordPress theme
 * and one of the two required files for a theme (the other being style.css).
 * As a single-page LP style theme, this acts as a fallback.
 */

get_header(); ?>

<main id="primary" class="site-main" style="padding: 120px 20px; text-align: center;">
    <section class="error-404 not-found">
        <header class="page-header">
            <h1 class="page-title">コンテンツが見つかりません。</h1>
        </header>

        <div class="page-content" style="margin-top: 24px;">
            <p>トップページをご確認ください。</p>
            <a href="<?php echo esc_url(home_url('/')); ?>" class="btn btn-web" style="display: inline-flex; margin-top: 20px;">トップページへ戻る</a>
        </div>
    </section>
</main>

<?php
get_footer();
