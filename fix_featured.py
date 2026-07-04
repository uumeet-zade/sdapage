with open('candidates.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix President
pres_old = """          <div class="featured-candidate-card">
            <div class="candidate-initials">TBD</div>
            <div class="candidate-name" data-i18n="cand-tbd">To Be Determined</div>
            <div class="candidate-role" data-i18n="role-pres">Presidential Candidate</div>
            <div class="candidate-constituency" data-i18n="const-nat">National</div>
            <div class="candidate-bio" data-i18n="bio-pres">Our presidential candidate will be announced soon.</div>
          </div>"""
pres_new = """          <div class="featured-candidate-card">
            <div class="candidate-initials">TBD</div>
            <div class="candidate-details">
              <div class="candidate-name" data-i18n="cand-tbd">To Be Determined</div>
              <div class="candidate-role" data-i18n="role-pres">Presidential Candidate</div>
              <div class="candidate-constituency" data-i18n="const-nat">National</div>
              <div class="candidate-bio" data-i18n="bio-pres">Our presidential candidate will be announced soon.</div>
            </div>
          </div>"""
content = content.replace(pres_old, pres_new)

# Fix Governor
gov_old = """          <div class="featured-candidate-card">
            <img class="candidate-image" src="portraits/Governors/SafiyaBethune.jpg" alt="Safiya Bethune-Fayyad" />
            <div class="candidate-name">Safiya Bethune-Fayyad</div>
            <div class="candidate-role" data-i18n="role-gov">Governor Candidate</div>
            <div class="candidate-constituency" data-i18n="const-ren">Reno</div>
            <div class="candidate-bio" data-i18n="bio-gov-ren">Running for Governor of Reno.</div>
          </div>"""
gov_new = """          <div class="featured-candidate-card">
            <img class="candidate-image" src="portraits/Governors/SafiyaBethune.jpg" alt="Safiya Bethune-Fayyad" />
            <div class="candidate-details">
              <div class="candidate-name">Safiya Bethune-Fayyad</div>
              <div class="candidate-role" data-i18n="role-gov">Governor Candidate</div>
              <div class="candidate-constituency" data-i18n="const-ren">Reno</div>
              <div class="candidate-bio" data-i18n="bio-gov-ren">Running for Governor of Reno.</div>
            </div>
          </div>"""
content = content.replace(gov_old, gov_new)

with open('candidates.html', 'w', encoding='utf-8') as f:
    f.write(content)
