"""
Comprehensive content population script for all Sauti website components.
This script ensures EVERY page component is editable through the CMS.

Usage:
    python populate_comprehensive_content.py
    OR
    python manage.py shell < populate_comprehensive_content.py
"""

import os
import django
import sys
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from content.models import SiteContent

COMPREHENSIVE_CONTENT = [

    # =========================
    # HOME PAGE – HERO SECTION
    # =========================
    {
        "key": "home_hero_headline",
        "label": "Home Hero Headline",
        "value": "TAKE NO CHANCES!",
        "page": "home",
        "type": "heading",
        "description": "Main hero headline on homepage"
    },
    {
        "key": "home_hero_subheadline",
        "label": "Home Hero Subheadline",
        "value": "Report a case now",
        "page": "home",
        "type": "heading",
        "description": "Hero subheadline"
    },
    {
        "key": "home_hero_cta_text",
        "label": "Home Hero CTA Text",
        "value": "Call {hotline} Toll Free",
        "page": "home",
        "type": "text",
        "description": "Hero call-to-action text with {hotline} placeholder"
    },
    {
        "key": "home_hero_call_button",
        "label": "Home Hero Call Button Text",
        "value": "Call Now",
        "page": "home",
        "type": "button",
        "description": "Call button text"
    },
    {
        "key": "home_hero_report_button",
        "label": "Home Hero Report Button Text",
        "value": "Report a case here",
        "page": "home",
        "type": "button",
        "description": "Report button text"
    },
    {
        "key": "home_hero_image_alt",
        "label": "Home Hero Image Alt Text",
        "value": "Ugandan mother protecting her children",
        "page": "home",
        "type": "text",
        "description": "Alt text for hero image"
    },
    {
        "key": "home_logo_sauti_alt",
        "label": "Home Logo Sauti Alt Text",
        "value": "Sauti 116 - Speak Up Against Violence",
        "page": "home",
        "type": "text",
        "description": "Alt text for Sauti logo"
    },
    {
        "key": "home_logo_uganda_alt",
        "label": "Home Logo Uganda Alt Text",
        "value": "Republic of Uganda",
        "page": "home",
        "type": "text",
        "description": "Alt text for Uganda logo"
    },

    # =========================
    # HOME PAGE – NEWS SECTION
    # =========================
    {
        "key": "home_news_badge_text",
        "label": "Home News Badge Text",
        "value": "Our Impact",
        "page": "home",
        "type": "text",
        "description": "Badge text for news section"
    },
    {
        "key": "home_news_title",
        "label": "Home News Section Title",
        "value": "Latest Stories & Updates",
        "page": "home",
        "type": "heading",
        "description": "Title for news section"
    },
    {
        "key": "home_news_description",
        "label": "Home News Section Description",
        "value": "Stay informed with the latest news from Sauti and our work across communities.",
        "page": "home",
        "type": "text",
        "description": "Description for news section"
    },
    {
        "key": "home_news_mock_featured_title",
        "label": "Home News Featured Article Title",
        "value": "Sauti 116 Expands Reach to Rural Areas",
        "page": "home",
        "type": "heading",
        "description": "Featured news article title"
    },
    {
        "key": "home_news_mock_featured_category",
        "label": "Home News Featured Category",
        "value": "Update",
        "page": "home",
        "type": "text",
        "description": "Featured article category"
    },
    {
        "key": "home_news_mock_featured_date",
        "label": "Home News Featured Date",
        "value": "Jan 12, 2026",
        "page": "home",
        "type": "text",
        "description": "Featured article date"
    },
    {
        "key": "home_news_mock_featured_text",
        "label": "Home News Featured Text",
        "value": "We are dedicated to ensuring every voice is heard. Our latest initiative focuses on reaching remote villages to provide immediate support.",
        "page": "home",
        "type": "text",
        "description": "Featured article summary"
    },
    {
        "key": "home_news_mock_side1_title",
        "label": "Home News Side Article 1 Title",
        "value": "School Outreach Programs Launching Soon",
        "page": "home",
        "type": "heading",
        "description": "Side article 1 title"
    },
    {
        "key": "home_news_mock_side1_category",
        "label": "Home News Side Article 1 Category",
        "value": "Program",
        "page": "home",
        "type": "text",
        "description": "Side article 1 category"
    },
    {
        "key": "home_news_mock_side1_date",
        "label": "Home News Side Article 1 Date",
        "value": "Jan 10, 2026",
        "page": "home",
        "type": "text",
        "description": "Side article 1 date"
    },
    {
        "key": "home_news_mock_side2_title",
        "label": "Home News Side Article 2 Title",
        "value": "Counselor Training Certification Complete",
        "page": "home",
        "type": "heading",
        "description": "Side article 2 title"
    },
    {
        "key": "home_news_mock_side2_category",
        "label": "Home News Side Article 2 Category",
        "value": "Achievement",
        "page": "home",
        "type": "text",
        "description": "Side article 2 category"
    },
    {
        "key": "home_news_mock_side2_date",
        "label": "Home News Side Article 2 Date",
        "value": "Jan 08, 2026",
        "page": "home",
        "type": "text",
        "description": "Side article 2 date"
    },
    {
        "key": "home_news_mock_side3_title",
        "label": "Home News Side Article 3 Title",
        "value": "Partnership with Ministry of Health",
        "page": "home",
        "type": "heading",
        "description": "Side article 3 title"
    },
    {
        "key": "home_news_mock_side3_category",
        "label": "Home News Side Article 3 Category",
        "value": "Partnership",
        "page": "home",
        "type": "text",
        "description": "Side article 3 category"
    },
    {
        "key": "home_news_mock_side3_date",
        "label": "Home News Side Article 3 Date",
        "value": "Jan 05, 2026",
        "page": "home",
        "type": "text",
        "description": "Side article 3 date"
    },

    # =========================
    # HOME PAGE – SOCIAL MEDIA
    # =========================
    {
        "key": "home_social_twitter_url",
        "label": "Social Media Twitter URL",
        "value": "https://x.com/sauti116",
        "page": "home",
        "type": "text",
        "description": "Twitter/X profile link"
    },
    {
        "key": "home_social_twitter_label",
        "label": "Social Media Twitter Label",
        "value": "X (formerly Twitter)",
        "page": "home",
        "type": "text",
        "description": "Aria label for Twitter"
    },
    {
        "key": "home_social_instagram_url",
        "label": "Social Media Instagram URL",
        "value": "https://instagram.com/sauti116",
        "page": "home",
        "type": "text",
        "description": "Instagram profile link"
    },
    {
        "key": "home_social_instagram_label",
        "label": "Social Media Instagram Label",
        "value": "Instagram",
        "page": "home",
        "type": "text",
        "description": "Aria label for Instagram"
    },
    {
        "key": "home_social_facebook_url",
        "label": "Social Media Facebook URL",
        "value": "https://facebook.com/Sauti116Helpline",
        "page": "home",
        "type": "text",
        "description": "Facebook profile link"
    },
    {
        "key": "home_social_facebook_label",
        "label": "Social Media Facebook Label",
        "value": "Facebook",
        "page": "home",
        "type": "text",
        "description": "Aria label for Facebook"
    },
    {
        "key": "home_social_tiktok_url",
        "label": "Social Media TikTok URL",
        "value": "https://tiktok.com/@sauti116",
        "page": "home",
        "type": "text",
        "description": "TikTok profile link"
    },
    {
        "key": "home_social_tiktok_label",
        "label": "Social Media TikTok Label",
        "value": "TikTok",
        "page": "home",
        "type": "text",
        "description": "Aria label for TikTok"
    },

    # =========================
    # HOME PAGE – PARTNERS SECTION
    # =========================
    {
        "key": "home_partners_title",
        "label": "Home Partners Section Title",
        "value": "Our Trusted Partners",
        "page": "home",
        "type": "heading",
        "description": "Partners section heading on homepage"
    },
    {
        "key": "home_partners_description",
        "label": "Home Partners Section Description",
        "value": "Working together with national and international organizations to protect every voice.",
        "page": "home",
        "type": "text",
        "description": "Partners section description on homepage"
    },

    # =========================
    # VIDEOS PAGE
    # =========================
    {
        "key": "videos_page_title",
        "label": "Videos Page Title",
        "value": "Sauti",
        "page": "videos",
        "type": "heading",
        "description": "Videos page main title"
    },
    {
        "key": "videos_page_title_highlight",
        "label": "Videos Page Title Highlight",
        "value": "Audio-Visuals",
        "page": "videos",
        "type": "heading",
        "description": "Videos page title highlight text"
    },
    {
        "key": "videos_search_heading",
        "label": "Videos Search Heading",
        "value": "Search Official Media",
        "page": "videos",
        "type": "heading",
        "description": "Videos page search section heading"
    },
    {
        "key": "videos_search_placeholder",
        "label": "Videos Search Placeholder",
        "value": "Search video archive...",
        "page": "videos",
        "type": "text",
        "description": "Videos search input placeholder"
    },
    {
        "key": "videos_search_button",
        "label": "Videos Search Button",
        "value": "Search",
        "page": "videos",
        "type": "button",
        "description": "Videos search button text"
    },

    # =========================
    # BLOG PAGE
    # =========================
    {
        "key": "blog_page_title",
        "label": "Blog Page Title",
        "value": "Updates",
        "page": "blog",
        "type": "heading",
        "description": "Blog page main title"
    },
    {
        "key": "blog_page_title_highlight",
        "label": "Blog Page Title Highlight",
        "value": "and blogs",
        "page": "blog",
        "type": "heading",
        "description": "Blog page title highlight"
    },
    {
        "key": "blog_search_placeholder",
        "label": "Blog Search Placeholder",
        "value": "Search articles...",
        "page": "blog",
        "type": "text",
        "description": "Blog search placeholder"
    },
    {
        "key": "blog_categories_dropdown",
        "label": "Blog Categories Dropdown",
        "value": "All Categories",
        "page": "blog",
        "type": "text",
        "description": "Blog categories dropdown default text"
    },
    {
        "key": "blog_all_button",
        "label": "Blog All Button",
        "value": "All",
        "page": "blog",
        "type": "button",
        "description": "Blog filter all button"
    },
    {
        "key": "blog_articles_button",
        "label": "Blog Articles Button",
        "value": "Articles",
        "page": "blog",
        "type": "button",
        "description": "Blog filter articles button"
    },
    {
        "key": "blog_loading",
        "label": "Blog Loading Message",
        "value": "Loading articles...",
        "page": "blog",
        "type": "text",
        "description": "Blog loading message"
    },

    # =========================
    # NEWS PAGE
    # =========================
    {
        "key": "news_page_title",
        "label": "News Page Title",
        "value": "Latest",
        "page": "news",
        "type": "heading",
        "description": "News page main title"
    },
    {
        "key": "news_page_title_highlight",
        "label": "News Page Title Highlight",
        "value": "News & Updates",
        "page": "news",
        "type": "heading",
        "description": "News page title highlight"
    },

    # =========================
    # RESOURCES PAGE
    # =========================
    {
        "key": "resources_page_title",
        "label": "Resources Page Title",
        "value": "Resources",
        "page": "resources",
        "type": "heading",
        "description": "Resources page main title"
    },
    {
        "key": "resources_page_title_highlight",
        "label": "Resources Page Title Highlight",
        "value": "& Downloads",
        "page": "resources",
        "type": "heading",
        "description": "Resources page title highlight"
    },
    {
        "key": "resources_search_placeholder",
        "label": "Resources Search Placeholder",
        "value": "Search resources...",
        "page": "resources",
        "type": "text",
        "description": "Resources search placeholder"
    },
    {
        "key": "resources_filter_all_categories",
        "label": "Resources All Categories",
        "value": "All Categories",
        "page": "resources",
        "type": "text",
        "description": "Resources filter all categories text"
    },

    # =========================
    # FAQS PAGE
    # =========================
    {
        "key": "faqs_page_title",
        "label": "FAQs Page Title",
        "value": "Frequently Asked",
        "page": "faqs",
        "type": "heading",
        "description": "FAQs page main title"
    },
    {
        "key": "faqs_page_title_highlight",
        "label": "FAQs Page Title Highlight",
        "value": "Questions",
        "page": "faqs",
        "type": "heading",
        "description": "FAQs page title highlight"
    },
    {
        "key": "faqs_search_placeholder",
        "label": "FAQs Search Placeholder",
        "value": "Search questions...",
        "page": "faqs",
        "type": "text",
        "description": "FAQs search placeholder"
    },

    # =========================
    # CONTACT PAGE
    # =========================
    {
        "key": "contact_page_title",
        "label": "Contact Page Title",
        "value": "Get in",
        "page": "contact",
        "type": "heading",
        "description": "Contact page main title"
    },
    {
        "key": "contact_page_title_highlight",
        "label": "Contact Page Title Highlight",
        "value": "Touch",
        "page": "contact",
        "type": "heading",
        "description": "Contact page title highlight"
    },
    {
        "key": "contact_page_description",
        "label": "Contact Page Description",
        "value": "We're here 24/7 to listen, support, and help. Reach out anytime.",
        "page": "contact",
        "type": "text",
        "description": "Contact page description"
    },

    # =========================
    # ABOUT PAGE – HERO SECTION
    # =========================
    {
        "key": "about_hero_badge",
        "label": "About Hero Badge Text",
        "value": "Who we are",
        "page": "about",
        "type": "text",
        "description": "Badge text in hero circle"
    },
    {
        "key": "about_hero_title",
        "label": "About Hero Title",
        "value": "About\nSauti 116",
        "page": "about",
        "type": "heading",
        "description": "Hero section title"
    },
    {
        "key": "about_hero_tagline",
        "label": "About Hero Tagline",
        "value": "From Uganda, For Children.",
        "page": "about",
        "type": "text",
        "description": "Hero section tagline"
    },
    {
        "key": "about_hero_right_column",
        "label": "About Hero Right Column Text",
        "value": "Every Child Matters",
        "page": "about",
        "type": "text",
        "description": "Right column text in grid"
    },

    # =========================
    # ABOUT PAGE – JOURNEY/TIMELINE
    # =========================
    {
        "key": "about_journey_title",
        "label": "About Journey Title",
        "value": "Our Journey",
        "page": "about",
        "type": "heading",
        "description": "Timeline section title"
    },
    {
        "key": "about_journey_subtitle",
        "label": "About Journey Subtitle",
        "value": "Milestones that define our commitment.",
        "page": "about",
        "type": "text",
        "description": "Timeline section subtitle"
    },

    # =========================
    # ABOUT PAGE – STATISTICS
    # =========================
    {
        "key": "about_stats_title",
        "label": "About Stats Title",
        "value": "REACH ACROSS THE NATION",
        "page": "about",
        "type": "heading",
        "description": "Statistics section title"
    },
    {
        "key": "about_stats_subtitle",
        "label": "About Stats Subtitle",
        "value": "How we are helping people across Uganda every day.",
        "page": "about",
        "type": "text",
        "description": "Statistics section subtitle"
    },

    # =========================
    # ABOUT PAGE – VALUES SECTION
    # =========================
    {
        "key": "about_values_title",
        "label": "About Values Title",
        "value": "Our Core Values",
        "page": "about",
        "type": "heading",
        "description": "Core values section title"
    },
    {
        "key": "about_values_badge",
        "label": "About Values Badge",
        "value": "Our Principles",
        "page": "about",
        "type": "text",
        "description": "Badge text for values section"
    },
    {
        "key": "about_values_description",
        "label": "About Values Description",
        "value": "Our core values guide every interaction, decision, and intervention. They are the foundation of our trust with the community.",
        "page": "about",
        "type": "text",
        "description": "Description of core values"
    },
    {
        "key": "about_values_stat_1_value",
        "label": "About Values Stat 1 Value",
        "value": "1M+",
        "page": "about",
        "type": "text",
        "description": "Statistics value 1"
    },
    {
        "key": "about_values_stat_1_label",
        "label": "About Values Stat 1 Label",
        "value": "Lives Impacted",
        "page": "about",
        "type": "text",
        "description": "Statistics label 1"
    },
    {
        "key": "about_values_stat_2_value",
        "label": "About Values Stat 2 Value",
        "value": "10+",
        "page": "about",
        "type": "text",
        "description": "Statistics value 2"
    },
    {
        "key": "about_values_stat_2_label",
        "label": "About Values Stat 2 Label",
        "value": "Years of Service",
        "page": "about",
        "type": "text",
        "description": "Statistics label 2"
    },

    # =========================
    # ABOUT PAGE – RESOLUTION SECTION
    # =========================
    {
        "key": "about_resolution_title",
        "label": "About Resolution Title",
        "value": "Path to Resolution",
        "page": "about",
        "type": "heading",
        "description": "Resolution path section title"
    },
    {
        "key": "about_resolution_subtitle",
        "label": "About Resolution Subtitle",
        "value": "How we ensure every case leads to safety.",
        "page": "about",
        "type": "text",
        "description": "Resolution path subtitle"
    },
    {
        "key": "about_resolution_central_goal",
        "label": "About Resolution Central Goal",
        "value": "Our Goal",
        "page": "about",
        "type": "text",
        "description": "Central goal text"
    },
    {
        "key": "about_resolution_central_text",
        "label": "About Resolution Central Text",
        "value": "The ultimate goal of our journey.",
        "page": "about",
        "type": "text",
        "description": "Central goal description"
    },
    {
        "key": "about_resolution_mobile_goal_text",
        "label": "About Resolution Mobile Goal Text",
        "value": "How We Work Together",
        "page": "about",
        "type": "text",
        "description": "Mobile goal text"
    },

    # =========================
    # ABOUT PAGE – TEAM SECTION
    # =========================
    {
        "key": "about_team_title",
        "label": "About Team Title",
        "value": "Meet Our Team",
        "page": "about",
        "type": "heading",
        "description": "Team section title"
    },
    {
        "key": "about_team_subtitle",
        "label": "About Team Subtitle",
        "value": "Dedicated professionals committed to the safety and well-being of every child.",
        "page": "about",
        "type": "text",
        "description": "Team section subtitle"
    },

    # =========================
    # PARTNERS PAGE
    # =========================
    {
        "key": "partners_cta_title",
        "label": "Partners CTA Title",
        "value": "How We Work Together",
        "page": "partners",
        "type": "heading",
        "description": "Partners CTA section title"
    },
    {
        "key": "partners_cta_text",
        "label": "Partners CTA Text",
        "value": "Interested in joining our mission to protect the children of Uganda? We are always looking for organizations that share our commitment.",
        "page": "partners",
        "type": "text",
        "description": "Partners CTA description"
    },
    {
        "key": "partners_cta_interest_button",
        "label": "Partners CTA Interest Button",
        "value": "Express Interest",
        "page": "partners",
        "type": "button",
        "description": "Button text to express partnership interest"
    },
    {
        "key": "partners_cta_learn_button",
        "label": "Partners CTA Learn Button",
        "value": "Learn About Our Impact",
        "page": "partners",
        "type": "button",
        "description": "Button text to learn about impact"
    },

    # =========================
    # CONTACT PAGE
    # =========================
    {
        "key": "contact_page_title",
        "label": "Contact Page Title",
        "value": "Get in Touch",
        "page": "contact",
        "type": "heading",
        "description": "Contact page main title"
    },
    {
        "key": "contact_page_subtitle",
        "label": "Contact Page Subtitle",
        "value": "We'd love to hear from you. Reach out to us today.",
        "page": "contact",
        "type": "text",
        "description": "Contact page subtitle"
    },

    # =========================
    # DONATE PAGE
    # =========================
    {
        "key": "donate_page_title",
        "label": "Donate Page Title",
        "value": "Support Our Mission",
        "page": "donate",
        "type": "heading",
        "description": "Donate page main title"
    },
    {
        "key": "donate_page_subtitle",
        "label": "Donate Page Subtitle",
        "value": "Your contribution helps us provide essential services.",
        "page": "donate",
        "type": "text",
        "description": "Donate page subtitle"
    },

    # =========================
    # OPERATIONS PAGE
    # =========================
    {
        "key": "operations_page_title",
        "label": "Operations Page Title",
        "value": "How We Operate",
        "page": "operations",
        "type": "heading",
        "description": "Operations page title"
    },
    {
        "key": "operations_page_description",
        "label": "Operations Page Description",
        "value": "Our comprehensive case management system ensures every report is handled with care and urgency.",
        "page": "operations",
        "type": "text",
        "description": "Operations page description"
    },

    # =========================
    # REPORTS PAGE
    # =========================
    {
        "key": "reports_page_title",
        "label": "Reports Page Title",
        "value": "Impact Reports",
        "page": "reports",
        "type": "heading",
        "description": "Reports page title"
    },
    {
        "key": "reports_page_description",
        "label": "Reports Page Description",
        "value": "View our comprehensive impact data and insights.",
        "page": "reports",
        "type": "text",
        "description": "Reports page description"
    },

    # =========================
    # BLOG PAGE
    # =========================
    {
        "key": "blog_page_title",
        "label": "Blog Page Title",
        "value": "Latest News & Articles",
        "page": "blog",
        "type": "heading",
        "description": "Blog page title"
    },
    {
        "key": "blog_page_description",
        "label": "Blog Page Description",
        "value": "Stay updated with our latest stories and insights.",
        "page": "blog",
        "type": "text",
        "description": "Blog page description"
    },

    # =========================
    # RESOURCES PAGE
    # =========================
    {
        "key": "resources_page_title",
        "label": "Resources Page Title",
        "value": "Resources & Materials",
        "page": "resources",
        "type": "heading",
        "description": "Resources page title"
    },
    {
        "key": "resources_page_description",
        "label": "Resources Page Description",
        "value": "Download guides, toolkits, and materials to support you.",
        "page": "resources",
        "type": "text",
        "description": "Resources page description"
    },

    # =========================
    # FAQs PAGE
    # =========================
    {
        "key": "faqs_page_title",
        "label": "FAQs Page Title",
        "value": "Frequently Asked Questions",
        "page": "faqs",
        "type": "heading",
        "description": "FAQs page title"
    },
    {
        "key": "faqs_page_description",
        "label": "FAQs Page Description",
        "value": "Find answers to common questions about our services.",
        "page": "faqs",
        "type": "text",
        "description": "FAQs page description"
    },

    # =========================
    # VIDEOS PAGE
    # =========================
    {
        "key": "videos_page_title",
        "label": "Videos Page Title",
        "value": "Video Gallery",
        "page": "videos",
        "type": "heading",
        "description": "Videos page title"
    },
    {
        "key": "videos_page_description",
        "label": "Videos Page Description",
        "value": "Watch our collection of educational and inspirational videos.",
        "page": "videos",
        "type": "text",
        "description": "Videos page description"
    },

    # =========================
    # HEADER / NAVIGATION
    # =========================
    {
        "key": "header_logo_alt",
        "label": "Header Logo Alt Text",
        "value": "Sauti 116 Logo",
        "page": "header",
        "type": "text",
        "description": "Alt text for site logo"
    },
    {
        "key": "header_hotline_label",
        "label": "Header Hotline Label",
        "value": "National Helpline",
        "page": "header",
        "type": "text",
        "description": "Label for hotline display"
    },

    # =========================
    # FOOTER
    # =========================
    {
        "key": "footer_brand_description",
        "label": "Footer Brand Description",
        "value": "Uganda's verified National Child Helpline. Providing 24/7 confidential support, guidance, and emergency intervention for all citizens.",
        "page": "footer",
        "type": "text",
        "description": "Description text in footer brand section"
    },
    {
        "key": "footer_copyright",
        "label": "Footer Copyright Text",
        "value": "© 2026 Sauti 116. Ministry of Gender, Labour and Social Development.",
        "page": "footer",
        "type": "text",
        "description": "Copyright notice in footer bottom bar"
    },
    {
        "key": "footer_country_label",
        "label": "Footer Country Label",
        "value": "Uganda",
        "page": "footer",
        "type": "text",
        "description": "Country label in footer"
    },
    {
        "key": "footer_hotline_label",
        "label": "Footer Hotline Label",
        "value": "Toll Free",
        "page": "footer",
        "type": "text",
        "description": "Label above hotline number in footer"
    },
    {
        "key": "footer_hotline_number",
        "label": "Footer Hotline Number Display",
        "value": "Call 116",
        "page": "footer",
        "type": "text",
        "description": "Hotline number display text in footer"
    },
    {
        "key": "footer_email_label",
        "label": "Footer Email Label",
        "value": "Email Us",
        "page": "footer",
        "type": "text",
        "description": "Label above email address in footer"
    },
    {
        "key": "footer_email_address",
        "label": "Footer Email Address",
        "value": "info@sauti116.ug",
        "page": "footer",
        "type": "text",
        "description": "Email address in footer"
    },
    {
        "key": "footer_menu_heading",
        "label": "Footer Menu Heading",
        "value": "Menu",
        "page": "footer",
        "type": "heading",
        "description": "Menu column heading in footer"
    },
    {
        "key": "footer_support_heading",
        "label": "Footer Support Heading",
        "value": "Support",
        "page": "footer",
        "type": "heading",
        "description": "Support column heading in footer"
    },
    {
        "key": "footer_contact_heading",
        "label": "Footer Contact Heading",
        "value": "Contact",
        "page": "footer",
        "type": "heading",
        "description": "Contact column heading in footer"
    },

    # =========================
    # GLOBAL SETTINGS
    # =========================
    {
        "key": "site_name",
        "label": "Site Name",
        "value": "Sauti 116",
        "page": "global",
        "type": "text",
        "description": "Application name"
    },
    {
        "key": "site_description",
        "label": "Site Description",
        "value": "Sauti 116: Uganda's National Helpline for rapid protection and response.",
        "page": "global",
        "type": "text",
        "description": "Meta description for SEO"
    },
    {
        "key": "hotline_number",
        "label": "Hotline Number",
        "value": "116",
        "page": "global",
        "type": "text",
        "description": "Main helpline phone number"
    },
    {
        "key": "operating_hours",
        "label": "Operating Hours",
        "value": "24/7",
        "page": "global",
        "type": "text",
        "description": "Operating hours definition"
    },

    # =========================
    # OPERATIONS & SERVICES PAGE
    # =========================
    {
        "key": "operations_page_title",
        "label": "Operations Page Title",
        "value": "How We",
        "page": "operations",
        "type": "heading",
        "description": "Operations page main title"
    },
    {
        "key": "operations_page_title_highlight",
        "label": "Operations Page Title Highlight",
        "value": "Operate",
        "page": "operations",
        "type": "heading",
        "description": "Operations page title highlight (colored text)"
    },
    {
        "key": "operations_page_subtitle",
        "label": "Operations Page Subtitle",
        "value": "Sauti is a Swahili word that means voice. Discover how we serve every citizen across Uganda 24/7.",
        "page": "operations",
        "type": "text",
        "description": "Operations page subtitle/description"
    },

    # Operations Section
    {
        "key": "operations_intro_text",
        "label": "Operations Introduction Text",
        "value": "Sauti is a Swahili word that means voice",
        "page": "operations",
        "type": "text",
        "description": "Operations section introduction"
    },
    {
        "key": "operations_shortcode_title",
        "label": "Operations Shortcode Title",
        "value": "Toll-Free Access",
        "page": "operations",
        "type": "heading",
        "description": "Shortcode feature title"
    },
    {
        "key": "operations_shortcode_text",
        "label": "Operations Shortcode Text",
        "value": "Operates on the short code 116 (toll free) accessible from any telecom network.",
        "page": "operations",
        "type": "text",
        "description": "Shortcode feature description"
    },
    {
        "key": "operations_availability_title",
        "label": "Operations Availability Title",
        "value": "24/7 Nationwide Coverage",
        "page": "operations",
        "type": "heading",
        "description": "Availability feature title"
    },
    {
        "key": "operations_availability_text",
        "label": "Operations Availability Text",
        "value": "Operational 24/7 and accessible from every part of the country.",
        "page": "operations",
        "type": "text",
        "description": "Availability feature description"
    },
    {
        "key": "operations_languages_title",
        "label": "Operations Languages Title",
        "value": "Multilingual Counselors",
        "page": "operations",
        "type": "heading",
        "description": "Languages feature title"
    },
    {
        "key": "operations_languages_text",
        "label": "Operations Languages Text",
        "value": "Our counselors speak a total of 26 local languages to serve every community.",
        "page": "operations",
        "type": "text",
        "description": "Languages feature description"
    },
    {
        "key": "operations_structure_title",
        "label": "Operations Structure Title",
        "value": "Two-Division Structure",
        "page": "operations",
        "type": "heading",
        "description": "Structure feature title"
    },
    {
        "key": "operations_structure_text",
        "label": "Operations Structure Text",
        "value": "Divided into 2 sections: call center for immediate response and case work for follow-up support.",
        "page": "operations",
        "type": "text",
        "description": "Structure feature description"
    },
    {
        "key": "operations_funding_title",
        "label": "Operations Funding Title",
        "value": "Funding & Support",
        "page": "operations",
        "type": "heading",
        "description": "Funding feature title"
    },
    {
        "key": "operations_funding_text",
        "label": "Operations Funding Text",
        "value": "Government of Uganda covers utility bills and 14% of salaries, while donors (UNICEF) support case management funds and project staff salaries.",
        "page": "operations",
        "type": "text",
        "description": "Funding feature description"
    },

    # Services Section
    {
        "key": "services_section_title",
        "label": "Services Section Title",
        "value": "Services We",
        "page": "operations",
        "type": "heading",
        "description": "Services section title"
    },
    {
        "key": "services_section_title_highlight",
        "label": "Services Section Title Highlight",
        "value": "Offer",
        "page": "operations",
        "type": "heading",
        "description": "Services section title highlight"
    },
    {
        "key": "services_section_subtitle",
        "label": "Services Section Subtitle",
        "value": "Comprehensive support services designed to protect and empower every voice in Uganda.",
        "page": "operations",
        "type": "text",
        "description": "Services section subtitle"
    },
    {
        "key": "service_counseling_title",
        "label": "Service - Telephone Counseling Title",
        "value": "Telephone Counseling",
        "page": "operations",
        "type": "heading",
        "description": "Telephone counseling service title"
    },
    {
        "key": "service_counseling_text",
        "label": "Service - Telephone Counseling Text",
        "value": "Professional counseling services available 24/7 through our toll-free helpline 116.",
        "page": "operations",
        "type": "text",
        "description": "Telephone counseling service description"
    },
    {
        "key": "service_walkin_title",
        "label": "Service - Walk-In Clients Title",
        "value": "Walk-In Support",
        "page": "operations",
        "type": "heading",
        "description": "Walk-in service title"
    },
    {
        "key": "service_walkin_text",
        "label": "Service - Walk-In Clients Text",
        "value": "Handle walk-in clients at our offices for face-to-face consultation and support.",
        "page": "operations",
        "type": "text",
        "description": "Walk-in service description"
    },
    {
        "key": "service_media_title",
        "label": "Service - Media Response Title",
        "value": "Media & U-Report Response",
        "page": "operations",
        "type": "heading",
        "description": "Media response service title"
    },
    {
        "key": "service_media_text",
        "label": "Service - Media Response Text",
        "value": "Respond to cases of violence against children and gender-based violence reported through media and U-report.",
        "page": "operations",
        "type": "text",
        "description": "Media response service description"
    },
    {
        "key": "service_guidance_title",
        "label": "Service - Information & Guidance Title",
        "value": "Information & Guidance",
        "page": "operations",
        "type": "heading",
        "description": "Information and guidance service title"
    },
    {
        "key": "service_guidance_text",
        "label": "Service - Information & Guidance Text",
        "value": "Provision of information and guidance on child care and protection matters.",
        "page": "operations",
        "type": "text",
        "description": "Information and guidance service description"
    },
    {
        "key": "service_referral_title",
        "label": "Service - Referral Title",
        "value": "Essential Service Referrals",
        "page": "operations",
        "type": "heading",
        "description": "Referral service title"
    },
    {
        "key": "service_referral_text",
        "label": "Service - Referral Text",
        "value": "Referral to essential services including healthcare, legal aid, and social support.",
        "page": "operations",
        "type": "text",
        "description": "Referral service description"
    },
    {
        "key": "service_community_title",
        "label": "Service - Community Sensitization Title",
        "value": "Community Sensitization",
        "page": "operations",
        "type": "heading",
        "description": "Community sensitization service title"
    },
    {
        "key": "service_community_text",
        "label": "Service - Community Sensitization Text",
        "value": "Community sensitization activities to raise awareness about child protection and GBV prevention.",
        "page": "operations",
        "type": "text",
        "description": "Community sensitization service description"
    },
    {
        "key": "service_chatbot_title",
        "label": "Service - MHPSS Chatbot Title",
        "value": "MHPSS Chatbot",
        "page": "operations",
        "type": "heading",
        "description": "MHPSS chatbot service title"
    },
    {
        "key": "service_chatbot_text",
        "label": "Service - MHPSS Chatbot Text",
        "value": "Mental Health and Psychosocial Support chatbot for immediate automated assistance.",
        "page": "operations",
        "type": "text",
        "description": "MHPSS chatbot service description"
    },

]


def populate_initial_content(clear_old=True):
    """
    Populate initial site content.

    Args:
        clear_old (bool): If True, delete ALL existing content before populating.
                         Set to False if you want to preserve custom edits.
    """
    created_count = 0
    updated_count = 0

    # Option: Clear ALL old content for fresh start
    if clear_old:
        old_count = SiteContent.objects.count()
        print(f"Clearing all {old_count} existing content entries...")
        SiteContent.objects.all().delete()
        print(f"✓ All content cleared")

    for item in COMPREHENSIVE_CONTENT:
        obj, created = SiteContent.objects.update_or_create(
            key=item["key"],
            defaults={
                "label": item["label"],
                "value": item["value"],
                "page": item["page"],
                "type": item["type"],
                "description": item["description"],
            }
        )
        if created:
            created_count += 1
        else:
            updated_count += 1

    print(f"✓ Content setup complete: {created_count} created, {updated_count} updated.")
    return created_count, updated_count


if __name__ == "__main__":
    populate_initial_content()
