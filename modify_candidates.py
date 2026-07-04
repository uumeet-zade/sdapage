import re

with open('candidates.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Filter HTML right before <div class="candidates-section">
filter_html = """
    <div class="candidate-filters event-filters" style="margin-top: -10px;">
      <button class="filter-btn active" data-filter="all" data-i18n="filter-all-cand">All Candidates</button>
      <button class="filter-btn" data-filter="executive" data-i18n="filter-exec">Executive</button>
      <button class="filter-btn" data-filter="senate" data-i18n="filter-senate">Senate</button>
      <button class="filter-btn" data-filter="house" data-i18n="filter-house">House (Constituency)</button>
      <button class="filter-btn" data-filter="list" data-i18n="filter-list">House (Party List)</button>
    </div>
    <div class="candidates-section">
"""
content = content.replace('<div class="candidates-section">', filter_html)

# 2. Extract and reorder categories
parts = content.split('<div class="candidates-category">')
prefix = parts[0]
categories = parts[1:]

# The last category will have the rest of the HTML attached to it.
# We can find where the <section class="pillars"... begins, which is after the last category.
last_cat_idx = len(categories) - 1
suffix_split = categories[last_cat_idx].split('<section class="pillars"')
categories[last_cat_idx] = suffix_split[0]
suffix = '\n  <section class="pillars"' + suffix_split[1]

pres_html = ""
senate_html = ""
house_const_html = ""
gov_html = ""
house_list_html = ""

for cat in categories:
    if 'data-i18n="cand-cat-pres"' in cat:
        # Change to featured
        cat = cat.replace('<div class="masonry-candidates">', '<div class="featured-candidates">')
        cat = cat.replace('<div class="candidate-card">', '<div class="featured-candidate-card">')
        pres_html = '<div class="candidates-category" data-category="executive">\n' + cat
    elif 'data-i18n="cand-cat-senate"' in cat:
        senate_html = '<div class="candidates-category" data-category="senate">\n' + cat
    elif 'data-i18n="cand-cat-house"' in cat:
        house_const_html = '<div class="candidates-category" data-category="house">\n' + cat
    elif 'data-i18n="cand-cat-gov"' in cat:
        # Change to featured
        cat = cat.replace('<div class="masonry-candidates">', '<div class="featured-candidates">')
        cat = cat.replace('<div class="candidate-card">', '<div class="featured-candidate-card">')
        gov_html = '<div class="candidates-category" data-category="executive">\n' + cat
    elif 'data-i18n="cand-cat-list"' in cat:
        house_list_html = '<div class="candidates-category" data-category="list">\n' + cat

# Reassemble in order: Pres, Gov, Senate, House Const, House List
new_content = prefix + pres_html + gov_html + senate_html + house_const_html + house_list_html + suffix

# 3. Add JavaScript for filtering
js_logic = """
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.filter-btn');
      const categories = document.querySelectorAll('.candidates-category');

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          // Remove active class from all buttons
          filterBtns.forEach(b => b.classList.remove('active'));
          // Add active class to clicked button
          btn.classList.add('active');

          const filterValue = btn.getAttribute('data-filter');

          categories.forEach(category => {
            const catType = category.getAttribute('data-category');
            if (filterValue === 'all' || catType === filterValue) {
              category.style.display = 'block';
              setTimeout(() => {
                category.style.opacity = '1';
                category.style.transform = 'translateY(0) scale(1)';
              }, 10);
            } else {
              category.style.opacity = '0';
              category.style.transform = 'translateY(20px) scale(0.95)';
              setTimeout(() => {
                category.style.display = 'none';
              }, 300); // Matches transition duration
            }
          });
        });
      });
    });
  </script>
</body>
"""

# Replace the previous modal logic completely, or just append this before </body>. 
# Wait, candidates.html already has <script> Modal Logic. Let's append to it.
existing_modal_script = """
      // Close on Escape key
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
          closeModal();
        }
      });
    });
"""
new_combined_script = existing_modal_script + """
    
    // Filter Logic
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.candidate-filters .filter-btn');
      const categories = document.querySelectorAll('.candidates-category');
      
      // Ensure smooth transitions
      categories.forEach(c => {
        c.style.transition = 'opacity 0.4s ease, transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.1)';
      });

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          filterBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');

          const filterValue = btn.getAttribute('data-filter');

          categories.forEach(category => {
            const catType = category.getAttribute('data-category');
            if (filterValue === 'all' || catType === filterValue) {
              category.style.display = 'block';
              setTimeout(() => {
                category.style.opacity = '1';
                category.style.transform = 'translateY(0) scale(1)';
              }, 10);
            } else {
              category.style.opacity = '0';
              category.style.transform = 'translateY(20px) scale(0.95)';
              setTimeout(() => {
                category.style.display = 'none';
              }, 300);
            }
          });
        });
      });
    });
"""

new_content = new_content.replace(existing_modal_script, new_combined_script)

with open('candidates.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
