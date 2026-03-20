<?php
/**
 * Template Name: Front Page
 */
get_header();
?>

<main id="primary" class="site-main">
    <?php get_template_part('template-parts/section', 'hero'); ?>
    <?php get_template_part('template-parts/section', 'about'); ?>
    <?php get_template_part('template-parts/section', 'worries'); ?>
    <?php get_template_part('template-parts/section', 'reviews'); ?>
    <?php get_template_part('template-parts/section', 'amenities'); ?>
    <?php get_template_part('template-parts/section', 'flow'); ?>
    <?php get_template_part('template-parts/section', 'policy'); ?>
    <?php get_template_part('template-parts/section', 'trainers'); ?>
    <?php get_template_part('template-parts/section', 'menu'); ?>
    <?php get_template_part('template-parts/section', 'info'); ?>
    <?php get_template_part('template-parts/section', 'access'); ?>
    <?php get_template_part('template-parts/section', 'faq'); ?>
</main>

<?php
get_footer();
