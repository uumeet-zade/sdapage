with open('events.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Filter HTML right before <div class="events-list">
filter_html = """
    <div class="event-filters">
      <button class="filter-btn active" data-filter="all" data-i18n="filter-all">All Events</button>
      <button class="filter-btn" data-filter="presidential" data-i18n="filter-pres">Presidential</button>
      <button class="filter-btn" data-filter="gov" data-i18n="filter-gov">Governors</button>
      <button class="filter-btn" data-filter="list" data-i18n="filter-list">Party List</button>
      <button class="filter-btn" data-filter="senate" data-i18n="filter-senate">Senate</button>
      <button class="filter-btn" data-filter="house" data-i18n="filter-house">House</button>
    </div>
    <div class="events-list">
"""
content = content.replace('<div class="events-list">', filter_html)

# 2. Add data-category to each event-card
parts = content.split('<div class="event-card">')
new_parts = [parts[0]]

for part in parts[1:]:
    # Determine category
    category = "all"
    if "Presidential Candidate" in part:
        category = "presidential"
    elif "Party List Unity Campaign" in part or "Legislative Strategy Meeting" in part or "Women in Leadership Forum" in part:
        category = "list"
    else:
        senate_names = ["Florence Marin", "Stephen Bratanovic", "Marcus Horvat", "Brezhnev Prigozhn"]
        if any(name in part for name in senate_names):
            category = "senate"
        else:
            house_names = ["Aldric von Reichel", "William Smith", "Sherwin Hildebrand", "Adam Scholz", "Dorothy Roosevelt"]
            if any(name in part for name in house_names):
                category = "house"
                
    new_parts.append(f'<div class="event-card" data-category="{category}">' + part)

content = "".join(new_parts)

# 3. Add 3 new Governor events for Safiya Bethune-Fayyad
new_events = """
        <div class="event-card" data-category="gov">
          <div class="event-date">
            <div class="event-date-month" data-i18n="month-aug">AUG</div>
            <div class="event-date-day">15</div>
          </div>
          <div class="event-details">
            <div class="event-title" data-i18n="ev-title-gov-1">Reno Governor Debate</div>
            <div class="event-location">📍 Reno City Hall</div>
            <div class="event-time">🕒 19:00 - 21:00</div>
            <div class="event-desc">
              <span data-i18n="event-speaker">Speaker:</span> <span> Safiya Bethune-Fayyad</span><br>
              <span data-i18n="ev-desc-gov-1">Watch Safiya debate on key issues concerning the future of Reno.</span>
            </div>
          </div>
          <div class="event-action">
            <button class="btn-outline" style="white-space: nowrap;" data-i18n="event-rsvp">RSVP</button>
          </div>
        </div>

        <div class="event-card" data-category="gov">
          <div class="event-date">
            <div class="event-date-month" data-i18n="month-sep">SEP</div>
            <div class="event-date-day">08</div>
          </div>
          <div class="event-details">
            <div class="event-title" data-i18n="ev-title-gov-2">Reno Community Townhall</div>
            <div class="event-location">📍 Reno Civic Center</div>
            <div class="event-time">🕒 18:00 - 20:00</div>
            <div class="event-desc">
              <span data-i18n="event-speaker">Speaker:</span> <span> Safiya Bethune-Fayyad</span><br>
              <span data-i18n="ev-desc-gov-2">An open discussion on local community initiatives and economic growth.</span>
            </div>
          </div>
          <div class="event-action">
            <button class="btn-outline" style="white-space: nowrap;" data-i18n="event-rsvp">RSVP</button>
          </div>
        </div>

        <div class="event-card" data-category="gov">
          <div class="event-date">
            <div class="event-date-month" data-i18n="month-oct">OCT</div>
            <div class="event-date-day">18</div>
          </div>
          <div class="event-details">
            <div class="event-title" data-i18n="ev-title-gov-3">Final Reno Rally</div>
            <div class="event-location">📍 Reno Grand Plaza</div>
            <div class="event-time">🕒 19:30 - 21:30</div>
            <div class="event-desc">
              <span data-i18n="event-speaker">Speaker:</span> <span> Safiya Bethune-Fayyad</span><br>
              <span data-i18n="ev-desc-gov-3">The final major rally for the Reno Governor campaign. Stand with Safiya!</span>
            </div>
          </div>
          <div class="event-action">
            <button class="btn-outline" style="white-space: nowrap;" data-i18n="event-rsvp">RSVP</button>
          </div>
        </div>
    </div>
"""
content = content.replace('    </div>\n  </div>\n\n\n  <footer>', new_events + '  </div>\n\n\n  <footer>')

# 4. Add JavaScript for filtering
js_logic = """
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.filter-btn');
      const events = document.querySelectorAll('.event-card');

      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          // Remove active class from all buttons
          filterBtns.forEach(b => b.classList.remove('active'));
          // Add active class to clicked button
          btn.classList.add('active');

          const filterValue = btn.getAttribute('data-filter');

          events.forEach(event => {
            if (filterValue === 'all' || event.getAttribute('data-category') === filterValue) {
              event.style.display = 'flex';
              setTimeout(() => {
                event.style.opacity = '1';
                event.style.transform = 'translateY(0) scale(1)';
              }, 10);
            } else {
              event.style.opacity = '0';
              event.style.transform = 'translateY(20px) scale(0.95)';
              setTimeout(() => {
                event.style.display = 'none';
              }, 300); // Matches transition duration
            }
          });
        });
      });
    });
  </script>
</body>
"""
content = content.replace('</body>', js_logic)

with open('events.html', 'w', encoding='utf-8') as f:
    f.write(content)
