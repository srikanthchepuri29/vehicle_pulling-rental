import os, re

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

rider_pages = {
    'portal_rider.html': 'home',
    'portal_rider_active.html': 'active',
    'portal_rider_earnings.html': 'earnings',
    'portal_rider_trips.html': 'trips',
    'portal_rider_profile.html': 'profile',
}

def get_navbar_html(active_key):
    home_active = "active-nav" if active_key == 'home' else ""
    active_active = "active-nav" if active_key == 'active' else ""
    earnings_active = "active-nav" if active_key == 'earnings' else ""
    trips_active = "active-nav" if active_key == 'trips' else ""
    profile_active = "active-nav" if active_key == 'profile' else ""

    return f"""    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg premium-navbar p-0">
        <div class="container-fluid">
            <div class="d-flex align-items-center">
                <a class="nav-menu-trigger dropdown-toggle mr-3" href="#" id="dashboardDropdown" data-toggle="dropdown" style="color: #fff; text-decoration: none;">
                    <i class="fas fa-bars"></i>
                </a>
                <div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; margin-top: 8px !important;">
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%) !important; padding: 10px 14px; color: #fff;">
                        <div class="d-flex align-items-center">
                            <div style="width:32px; height:32px; border-radius:10px; background:rgba(255,255,255,.22); display:flex; align-items:center; justify-content:center; margin-right:10px;">
                                <i class="fas fa-motorcycle" style="font-size:14px; color:#fff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold" style="font-size:0.82rem; color:#fff;">Chauffeur Console</h6>
                                <small class="text-white-50" style="font-size:0.65rem;">Live Dispatch</small>
                            </div>
                        </div>
                        <span class="badge" style="background:rgba(255,255,255,.25); color:#fff; font-size:0.6rem; padding:3px 6px; border-radius:8px;">Active Rider</span>
                    </div>

                    <div class="py-1">
                        <div class="dropdown-section-label">Rider Profile &amp; Controls</div>
                        <a class="premium-dropdown-item item-colored-theme" href="{{% url 'portal_rider_profile' %}}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(245,158,11,.2); color:#d97706;"><i class="fas fa-user-cog"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Profile &amp; Settings</div>
                                    <div class="dropdown-item-sub">Captain Features &amp; Image</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(245,158,11,.15); color:#d97706; font-size:0.58rem; padding:2px 5px; border-radius:5px;"><i class="fas fa-shield-alt mr-1"></i>Verified</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="{{% url 'portal_rider_active' %}}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(2,132,199,.14); color:#0284c7;"><i class="fas fa-crosshairs"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Active Ride Ticket</div>
                                    <div class="dropdown-item-sub">Live Route GPS</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(2,132,199,.15); color:#0284c7; font-size:0.58rem; padding:2px 5px; border-radius:5px;">On Duty</span>
                        </a>
                        <a class="premium-dropdown-item" href="{{% url 'portal_rider_trips' %}}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(99,102,241,.14); color:#6366f1;"><i class="fas fa-history"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Trip History</div>
                                    <div class="dropdown-item-sub">Completed Trips Log</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(99,102,241,.12); color:#4f46e5; font-size:0.58rem; padding:2px 5px; border-radius:5px;">Logs</span>
                        </a>
                        <a class="premium-dropdown-item" href="{{% url 'portal_rider_earnings' %}}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(16,185,129,.14); color:#10b981;"><i class="fas fa-wallet"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Earnings Ledger</div>
                                    <div class="dropdown-item-sub">Payouts &amp; Analytics</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(16,185,129,.15); color:#059669; font-size:0.58rem; padding:2px 5px; border-radius:5px;">Payouts</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="/">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(139,92,246,.14); color:#8b5cf6;"><i class="fas fa-exchange-alt"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Exit to User Portal</div>
                                    <div class="dropdown-item-sub">Return to Home</div>
                                </div>
                            </div>
                            <i class="fas fa-chevron-right text-muted" style="font-size:0.6rem; opacity:0.4;"></i>
                        </a>
                        <a class="premium-dropdown-item item-colored-logout" href="{{% url 'portal_logout' %}}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(239,68,68,.2); color:#dc2626;"><i class="fas fa-sign-out-alt"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Logout Session</div>
                                    <div class="dropdown-item-sub">Sign out securely</div>
                                </div>
                            </div>
                            <i class="fas fa-power-off text-danger" style="font-size:0.75rem; opacity:0.8;"></i>
                        </a>
                    </div>
                </div>

                <a class="navbar-brand font-weight-bold" href="{{% url 'portal_rider' %}}">
                    <i class="fas fa-motorcycle mr-2"></i>Chauffeur Console
                </a>
            </div>

            <!-- Standardized Rider Home Page Names -->
            <div class="d-flex align-items-center">
                <a class="nav-link {home_active}" href="{{% url 'portal_rider' %}}"><i class="fas fa-tachometer-alt mr-1"></i> Rider Home</a>
                <a class="nav-link {active_active}" href="{{% url 'portal_rider_active' %}}"><i class="fas fa-crosshairs mr-1"></i> Active Ride Ticket</a>
                <a class="nav-link {earnings_active}" href="{{% url 'portal_rider_earnings' %}}"><i class="fas fa-wallet mr-1"></i> Earnings Ledger</a>
                <a class="nav-link {trips_active}" href="{{% url 'portal_rider_trips' %}}"><i class="fas fa-history mr-1"></i> Trip History</a>
                <a class="nav-link {profile_active}" href="{{% url 'portal_rider_profile' %}}"><i class="fas fa-user-cog mr-1"></i> Profile &amp; Settings</a>
            </div>

            <!-- Compact Duty Toggle Button on Far Right Corner -->
            <div class="ml-auto d-flex align-items-center">
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-2 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1px solid #ffffff; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4); font-size: 0.72rem; display: inline-flex; align-items: center; gap: 4px; line-height: 1;">
                    <span id="dutyPulseDot" class="live-dot"></span>
                    <span id="dutyBtnText">ON DUTY</span>
                </button>
            </div>
        </div>
    </nav>"""

for fname, active_key in rider_pages.items():
    fpath = os.path.join(templates_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        nav_start = content.find('<nav class="navbar')
        if nav_start != -1:
            nav_end = content.find('</nav>', nav_start)
            if nav_end != -1:
                new_nav = get_navbar_html(active_key)
                content = content[:nav_start] + new_nav + content[nav_end + 6:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated navbar in {fname}")

print("Successfully standardized navbar design and Rider Home page names across all rider dashboard pages!")
