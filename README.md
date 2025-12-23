# COGVL Workshop Website

Website for the COGVL: Cognitive Foundations for Multimodal Models workshop at CVPR 2026.

## Setup

This is a Jekyll site designed to run on GitHub Pages.

### Local Development

1. Install Ruby and Bundler (if not already installed)
2. Install dependencies:
   ```bash
   bundle install
   ```
3. Run the Jekyll server:
   ```bash
   bundle exec jekyll serve
   ```
4. Open your browser to `http://localhost:4000`

### GitHub Pages Deployment

This site is configured to work with GitHub Pages. Simply push to the repository and GitHub Pages will automatically build and deploy the site.

## Structure

- `_config.yml` - Jekyll configuration
- `_layouts/` - Page layouts
- `_includes/` - Reusable components (header, footer)
- `assets/css/` - Stylesheets
- `static/images/` - Images and assets
- `index.md` - Landing page
- `call-for-papers.md` - Call for Papers page
- `blackswan-challenge.md` - BlackSwan Challenge page
- `faq.md` - FAQ page

## Notes

- The site uses DM Serif Text for headings and Figtree for body text
- Font Awesome icons are loaded via CDN
- The site is designed to be lightweight and fast-loading
- All organizer photos should be placed in `static/images/organizers/`

