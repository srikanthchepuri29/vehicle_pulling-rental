import os, re

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

rider_pages = {
    'portal_rider.html': 'home',
    'portal_rider_active.html': 'active',
    'portal_rider_trips.html': 'trips',
    'portal_rider_earnings.html': 'earnings',
    'portal_rider_profile.html': 'profile',
}

def get_updated_dropdown_navbar(active_key):
    home_cls = "nav-link active-nav" if active_key == "home" else "nav-link"
    active_cls = "nav-link active-nav" if active_key == "active" else "nav-link"
    trips_cls = "nav-link active-nav" if active_key == "trips" else "nav-link"
    earnings_cls = "nav-link active-nav" if active_key == "earnings" else "nav-link"

    return f"""    <!-- Rider Header Navbar -->
    <nav class="navbar navbar-expand-lg premium-navbar p-0">
        <div class="container-fluid d-flex align-items-center justify-content-between">
            <div class="d-flex align-items-center">
                <!-- Dropdown Menu Icon (Hamburger) -->
                <div class="dropdown mr-2 d-flex align-items-center">
                    <a class="nav-menu-trigger dropdown-toggle" href="#" id="dashboardDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: #ffffff; text-decoration: none;">
                        <i class="fas fa-bars"></i>
                    </a>
                    <div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 295px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 16px; border: 1.5px solid rgba(245, 158, 11, 0.4); box-shadow: 0 16px 45px rgba(245, 158, 11, 0.18), 0 4px 15px rgba(0,0,0,0.08); background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px);">
                        <!-- Dynamic Compact Menu Header -->
                        <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%) !important; padding: 10px 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.18) !important;">
                            <div class="d-flex align-items-center">
                                <div style="width: 32px; height: 32px; border-radius: 10px; background: rgba(255,255,255,0.22); display: flex; align-items: center; justify-content: center; margin-right: 10px; backdrop-filter: blur(4px); overflow:hidden;">
                                    {{% if user_profile and user_profile.image %}}
                                    <img src="{{{{ user_profile.image.url }}}}" id="navDropdownAvatar" style="width:100%; height:100%; object-fit:cover;">
                                    {{% else %}}
                                    <i class="fas fa-motorcycle" style="font-size: 14px; color: #ffffff;"></i>
                                    {{% endif %}}
                                </div>
                                <div>
                                    <h6 class="mb-0 font-weight-bold text-white" style="font-size: 0.82rem; line-height: 1.1;">{{{{ user.get_full_name|default:user.username }}}}</h6>
                                    <small class="text-white-50" style="font-size: 0.65rem;"><i class="fas fa-circle text-light mr-1" style="font-size: 5px;"></i>Live Dispatch</small>
                                </div>
                            </div>
                            <span class="badge" style="background: rgba(255,255,255,0.25); color: #ffffff; font-size: 0.6rem; padding: 3px 6px; border-radius: 8px; font-weight: 700;">Active Rider</span>
                        </div>

                        <div class="py-1">
                            <div class="dropdown-section-label" style="color: #d97706 !important;">Rider Profile &amp; Controls</div>
                            <a class="premium-dropdown-item item-colored-theme-amber" href="{{% url 'portal_rider_profile' %}}">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(245, 158, 11, 0.2); color: #d97706;">
                                        <i class="fas fa-user-cog"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Profile &amp; Settings</div>
                                        <div class="dropdown-item-sub">Rider Details &amp; Image</div>
                                    </div>
                                </div>
                                <span class="badge" style="background: rgba(245, 158, 11, 0.15); color: #d97706; font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; font-weight: 700;"><i class="fas fa-shield-alt mr-1"></i>Verified</span>
                            </a>

                            <div class="dropdown-divider-premium"></div>

                            <a class="premium-dropdown-item" href="{{% url 'portal_rider_active' %}}">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(2, 132, 199, 0.14); color: #0284c7;">
                                        <i class="fas fa-crosshairs"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Active Ride Ticket</div>
                                        <div class="dropdown-item-sub">Live Route GPS</div>
                                    </div>
                                </div>
                                <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(2, 132, 199, 0.15); color: #0284c7; font-weight: 700;"><i class="fas fa-satellite-dish mr-1"></i>On Duty</span>
                            </a>
                            <a class="premium-dropdown-item" href="{{% url 'portal_rider_trips' %}}">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(99, 102, 241, 0.14); color: #6366f1;">
                                        <i class="fas fa-history"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Trip History</div>
                                        <div class="dropdown-item-sub">Completed Trips Log</div>
                                    </div>
                                </div>
                                <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(99, 102, 241, 0.12); color: #4f46e5; font-weight: 700;">Logs</span>
                            </a>
                            <a class="premium-dropdown-item" href="{{% url 'portal_rider_earnings' %}}">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(16, 185, 129, 0.14); color: #10b981;">
                                        <i class="fas fa-wallet"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Earnings Ledger</div>
                                        <div class="dropdown-item-sub">Payouts &amp; Analytics</div>
                                    </div>
                                </div>
                                <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(16, 185, 129, 0.15); color: #059669; font-weight: 700;">Payouts</span>
                            </a>

                            <div class="dropdown-divider-premium"></div>

                            <div class="dropdown-section-label" style="color: #d97706 !important;">Captain Fleet Utilities</div>
                            <a class="premium-dropdown-item" href="#" onclick="if(typeof showToast==='function') showToast('Surge Heatmap: Central Hub 2.1x, Airport Road 1.8x Active'); return false;">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(245, 158, 11, 0.15); color: #d97706;">
                                        <i class="fas fa-fire-alt"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Surge Heatmap &amp; Demand</div>
                                        <div class="dropdown-item-sub">High Fare Hotspots</div>
                                    </div>
                                </div>
                                <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(245, 158, 11, 0.18); color: #d97706; font-weight: 700;">+2.1x</span>
                            </a>
                            <a class="premium-dropdown-item" href="#" onclick="if(typeof showToast==='function') showToast('Fuel Ledger: Today ₹320 Reimbursement Auto-Claimed'); return false;">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(14, 165, 233, 0.14); color: #0ea5e9;">
                                        <i class="fas fa-gas-pump"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Fuel &amp; Reimbursement</div>
                                        <div class="dropdown-item-sub">Auto Mileage &amp; Toll Log</div>
                                    </div>
                                </div>
                                <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(14, 165, 233, 0.14); color: #0284c7; font-weight: 700;">Claimed</span>
                            </a>
                            <a class="premium-dropdown-item" href="#" onclick="if(typeof showToast==='function') showToast('Captain Hotline: Connecting to 24/7 Support Operator...'); return false;">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(168, 85, 247, 0.14); color: #a855f7;">
                                        <i class="fas fa-headset"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">24x7 Captain Helpline</div>
                                        <div class="dropdown-item-sub">Roadside &amp; Emergency SOS</div>
                                    </div>
                                </div>
                                <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(168, 85, 247, 0.14); color: #9333ea; font-weight: 700;">24/7 SOS</span>
                            </a>

                            <div class="dropdown-divider-premium"></div>

                            <a class="premium-dropdown-item item-colored-logout" href="{{% url 'portal_logout' %}}">
                                <div class="d-flex align-items-center">
                                    <div class="dropdown-icon-box" style="background: rgba(239, 68, 68, 0.2); color: #dc2626;">
                                        <i class="fas fa-sign-out-alt"></i>
                                    </div>
                                    <div>
                                        <div class="dropdown-item-title">Logout Session</div>
                                        <div class="dropdown-item-sub">Sign out securely</div>
                                    </div>
                                </div>
                                <i class="fas fa-power-off text-danger" style="font-size: 0.75rem; opacity: 0.8;"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <a class="navbar-brand font-weight-bold mr-3" href="{{% url 'portal_rider' %}}" style="font-size: 1.05rem;">
                    <i class="fas fa-motorcycle mr-1"></i>Chauffeur Console
                </a>

                <div class="d-flex align-items-center ml-2">
                    <a class="{home_cls}" href="{{% url 'portal_rider' %}}"><i class="fas fa-tachometer-alt mr-1"></i> Rider Home</a>
                    <a class="{active_cls}" href="{{% url 'portal_rider_active' %}}"><i class="fas fa-crosshairs mr-1"></i> Active Ride Ticket</a>
                    <a class="{trips_cls}" href="{{% url 'portal_rider_trips' %}}"><i class="fas fa-history mr-1"></i> Trip History</a>
                    <a class="{earnings_cls}" href="{{% url 'portal_rider_earnings' %}}"><i class="fas fa-wallet mr-1"></i> Earnings Ledger</a>
                </div>
            </div>

            <!-- Far Right: Exit Button & Duty Toggle -->
            <div class="d-flex align-items-center ml-auto" style="gap: 10px;">
                <a href="/" class="btn btn-sm font-weight-bold px-2 py-1 rounded-pill" style="background: rgba(255,255,255,0.2); color: #ffffff; border: 1px solid #ffffff; font-size: 0.72rem; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; line-height: 1;">
                    <i class="fas fa-sign-out-alt"></i> Exit
                </a>
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-2 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1px solid #ffffff; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4); font-size: 0.72rem; display: inline-flex; align-items: center; gap: 4px; line-height: 1;">
                    <span id="dutyPulseDot" class="live-dot" style="width: 6px; height: 6px; background-color: #ffffff;"></span>
                    <span id="dutyBtnText">ON DUTY</span>
                </button>
            </div>
        </div>
    </nav>"""

for fname, key in rider_pages.items():
    fpath = os.path.join(templates_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        nav_start = content.find('<nav class="navbar')
        if nav_start != -1:
            nav_end = content.find('</nav>', nav_start)
            if nav_end != -1:
                new_nav = get_updated_dropdown_navbar(key)
                content = content[:nav_start] + new_nav + content[nav_end + 6:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated dropdown menu in {fname}")

print("Dropdown menu updated with 3 new Captain features and Exit link removed across all 5 templates!")
