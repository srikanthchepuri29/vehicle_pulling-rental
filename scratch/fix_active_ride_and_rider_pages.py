import os

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

# 1. Clean, Working portal_rider_active.html
rider_active_html = """{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Chauffeur Console - Active Ride Navigation</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min-1.css'%}">
    <link rel="stylesheet" href="{% static 'css/premium_home.css' %}">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        body { padding-top: 80px !important; font-family: 'Rubik', sans-serif; background-color: #fffbeb !important; color: #0f172a !important; }
        .live-dot { width:6px; height:6px; background:#ffffff; border-radius:50%; display:inline-block; }
        .premium-navbar { background-color:#f59e0b !important; border:none !important; box-shadow:0 4px 15px rgba(245,158,11,.3) !important; position:fixed !important; top:0; left:0; right:0; z-index:1030; padding:0 !important; }
        .premium-navbar .container-fluid { height:60px !important; padding:0 16px !important; display:flex !important; align-items:center !important; }
        .navbar-brand { color:#fff !important; font-size:1.15rem !important; font-weight:700 !important; display:flex !important; align-items:center !important; gap:8px; text-decoration:none !important; }
        .premium-navbar .nav-link { color:#fff !important; font-weight:500 !important; font-size:14px !important; padding:0 16px !important; height:60px !important; display:flex !important; align-items:center; text-decoration:none !important; transition:.25s; }
        .premium-navbar .nav-link:hover { background:rgba(255,255,255,.16) !important; }
        .premium-navbar .nav-link.active-nav { background:rgba(0,0,0,.12) !important; font-weight:700 !important; }

        /* Dynamic Dropdown Container */
        .premium-user-dropdown {
            min-width: 295px !important; border-radius: 16px !important; overflow: hidden !important; padding: 0 !important; margin-top: 8px !important;
            border: 1.5px solid rgba(245, 158, 11, 0.4) !important; box-shadow: 0 16px 45px rgba(245, 158, 11, 0.18), 0 4px 15px rgba(0,0,0,0.08) !important;
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px) !important;
        }
        .dropdown-section-label { font-size: 0.6rem !important; font-weight: 800 !important; letter-spacing: 0.8px !important; text-transform: uppercase !important; padding: 4px 14px 2px 14px !important; color: #d97706 !important; }
        .premium-dropdown-item { display: flex !important; align-items: center !important; justify-content: space-between !important; padding: 5px 10px !important; text-decoration: none !important; transition: all 0.2s ease !important; border-radius: 8px !important; margin: 1px 6px !important; width: calc(100% - 12px) !important; }
        .premium-dropdown-item:hover { transform: translateX(3px) !important; text-decoration: none !important; }
        .dropdown-icon-box { width: 28px !important; height: 28px !important; border-radius: 8px !important; display: flex !important; align-items: center !important; justify-content: center !important; font-size: 0.8rem !important; margin-right: 8px !important; }

        .item-colored-theme { background: rgba(245, 158, 11, 0.14) !important; }
        .item-colored-theme .dropdown-item-title { color: #d97706 !important; font-weight: 750 !important; }
        .item-colored-logout { background: rgba(239, 68, 68, 0.14) !important; }
        .item-colored-logout .dropdown-item-title { color: #dc2626 !important; font-weight: 750 !important; }
        .dropdown-item-title { font-size: 0.8rem !important; font-weight: 750 !important; color: #0f172a !important; margin-bottom: 0 !important; }
        .dropdown-item-sub { font-size: 0.65rem !important; color: #64748b !important; }
        .dropdown-divider-premium { height: 1px !important; margin: 3px 10px !important; background: rgba(226, 232, 240, 0.8) !important; }

        #rider-map { height: 420px; width: 100%; border-radius: 16px; border: 1.5px solid rgba(245,158,11,.3); }
        .active-card { background:#fff; border-radius:20px; border:1.5px solid rgba(245,158,11,.25); border-top:4px solid #f59e0b; box-shadow:0 8px 24px rgba(15,23,42,.06); padding:24px; margin-bottom:24px; }
    </style>
</head>
<body>
    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg premium-navbar p-0">
        <div class="container-fluid">
            <div class="d-flex align-items-center">
                <a class="nav-menu-trigger dropdown-toggle mr-3" href="#" id="dashboardDropdown" data-toggle="dropdown" style="color: #fff;">
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
                        <a class="premium-dropdown-item item-colored-theme" href="{% url 'portal_rider_profile' %}">
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

                        <a class="premium-dropdown-item" href="{% url 'portal_rider_active' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(2,132,199,.14); color:#0284c7;"><i class="fas fa-motorcycle"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Active Rides</div>
                                    <div class="dropdown-item-sub">Live Trip Dashboard</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(2,132,199,.15); color:#0284c7; font-size:0.58rem; padding:2px 5px; border-radius:5px;">On Duty</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rider_trips' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(99,102,241,.14); color:#6366f1;"><i class="fas fa-history"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Ride History</div>
                                    <div class="dropdown-item-sub">Completed Trips Log</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(99,102,241,.12); color:#4f46e5; font-size:0.58rem; padding:2px 5px; border-radius:5px;">Logs</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rider_earnings' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(16,185,129,.14); color:#10b981;"><i class="fas fa-wallet"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Total Earnings</div>
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
                        <a class="premium-dropdown-item item-colored-logout" href="{% url 'portal_logout' %}">
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

                <a class="navbar-brand font-weight-bold" href="{% url 'portal_rider' %}">
                    <i class="fas fa-motorcycle mr-2"></i>Chauffeur Console
                </a>
            </div>

            <div class="d-flex align-items-center">
                <a class="nav-link" href="{% url 'portal_rider' %}"><i class="fas fa-tachometer-alt mr-1"></i> Dashboard</a>
                <a class="nav-link active-nav" href="{% url 'portal_rider_active' %}"><i class="fas fa-motorcycle mr-1"></i> Active Rides</a>
                <a class="nav-link" href="{% url 'portal_rider_trips' %}"><i class="fas fa-history mr-1"></i> Trips</a>
                <a class="nav-link" href="{% url 'portal_rider_earnings' %}"><i class="fas fa-wallet mr-1"></i> Earnings</a>
                <a class="nav-link" href="{% url 'portal_rider_profile' %}"><i class="fas fa-user-cog mr-1"></i> Profile &amp; Settings</a>
            </div>

            <!-- Compact Duty Toggle Button -->
            <div class="ml-auto d-flex align-items-center">
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-2 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1px solid #ffffff; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4); font-size: 0.72rem; display: inline-flex; align-items: center; gap: 4px; line-height: 1;">
                    <span id="dutyPulseDot" class="live-dot"></span>
                    <span id="dutyBtnText">ON DUTY</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Main Container -->
    <div class="container py-4">
        <!-- Off Duty Notice Banner -->
        <div id="riderOffDutyNotice" class="text-center py-5 my-4 bg-white rounded-xl shadow-sm border" style="display: none; border-color: rgba(239, 68, 68, 0.3) !important;">
            <div style="width: 70px; height: 70px; border-radius: 50%; background: rgba(239, 68, 68, 0.1); color: #ef4444; display: inline-flex; align-items: center; justify-content: center; font-size: 2rem; margin-bottom: 16px;">
                <i class="fas fa-power-off"></i>
            </div>
            <h4 class="font-weight-bold" style="color: #0f172a;">You Are Currently OFF DUTY</h4>
            <p class="text-muted" style="max-width: 480px; margin: 0 auto 20px auto; font-size: 0.9rem;">You are currently off duty. Switch back to <strong>ON DUTY</strong> in the navbar to view active passenger routes.</p>
            <button onclick="toggleRiderDutyState()" class="btn font-weight-bold px-4 py-2 rounded-pill shadow-sm" style="background: #10b981; color: #fff; border: none;">
                <i class="fas fa-toggle-on mr-2"></i> Switch ON DUTY Now
            </button>
        </div>

        <div id="riderRidesSection">
            {% if active_ride %}
            <div class="row">
                <div class="col-lg-8 mb-4">
                    <div class="active-card p-3">
                        <div class="d-flex align-items-center justify-content-between mb-3">
                            <h5 class="font-weight-bold mb-0 text-dark"><i class="fas fa-satellite-dish text-warning mr-2"></i>Live GPS Navigation</h5>
                            <span class="badge badge-warning text-dark font-weight-bold">Ticket #RS-{{ active_ride.id }}</span>
                        </div>
                        <div id="rider-map"></div>
                    </div>
                </div>

                <div class="col-lg-4 mb-4">
                    <div class="active-card">
                        <h5 class="font-weight-bold mb-3" style="color:#d97706;"><i class="fas fa-ticket-alt mr-2"></i>Passenger Ticket Details</h5>
                        
                        <div class="py-2 border-bottom">
                            <small class="text-muted font-weight-bold">PASSENGER NAME</small>
                            <div class="font-weight-bold" style="font-size:1rem; color:#0f172a;">{{ active_ride.user.username }}</div>
                        </div>

                        <div class="py-2 border-bottom">
                            <small class="text-muted font-weight-bold">PICKUP LOCATION</small>
                            <div class="font-weight-bold text-success" style="font-size:0.9rem;"><i class="fas fa-circle mr-1"></i> {{ active_ride.pickup }}</div>
                        </div>

                        <div class="py-2 border-bottom">
                            <small class="text-muted font-weight-bold">DROP DESTINATION</small>
                            <div class="font-weight-bold text-danger" style="font-size:0.9rem;"><i class="fas fa-map-marker-alt mr-1"></i> {{ active_ride.drop }}</div>
                        </div>

                        <div class="d-flex align-items-center justify-content-between py-3">
                            <div>
                                <small class="text-muted font-weight-bold">ESTIMATED FARE</small>
                                <div class="font-weight-bold text-success" style="font-size:1.4rem;">₹{{ active_ride.price }}</div>
                            </div>
                            <span class="badge badge-primary px-3 py-2 font-weight-bold">{{ active_ride.status }}</span>
                        </div>

                        <form method="POST" action="{% url 'api_update_ride_status' active_ride.id %}" class="mt-2">
                            {% csrf_token %}
                            {% if active_ride.status == 'Accepted' %}
                            <input type="hidden" name="status" value="Arrived">
                            <button type="submit" class="btn btn-warning btn-block text-dark font-weight-bold py-2 rounded-pill shadow-sm" style="background:#f59e0b; border:none;">
                                <i class="fas fa-map-pin mr-1"></i> Mark Arrived at Pickup
                            </button>
                            {% elif active_ride.status == 'Arrived' %}
                            <input type="hidden" name="status" value="In_Progress">
                            <button type="submit" class="btn btn-primary btn-block font-weight-bold py-2 rounded-pill shadow-sm">
                                <i class="fas fa-play mr-1"></i> Start Passenger Trip
                            </button>
                            {% elif active_ride.status == 'In_Progress' %}
                            <input type="hidden" name="status" value="Completed">
                            <button type="submit" class="btn btn-success btn-block font-weight-bold py-2 rounded-pill shadow-sm">
                                <i class="fas fa-check-circle mr-1"></i> Complete Trip &amp; Collect Cash
                            </button>
                            {% endif %}
                        </form>
                    </div>
                </div>
            </div>
            {% else %}
            <div class="active-card text-center py-5">
                <i class="fas fa-motorcycle mb-3" style="font-size:3rem; color:#f59e0b; opacity:0.4;"></i>
                <h4 class="font-weight-bold" style="color:#0f172a;">No Active Ride Assigned Right Now</h4>
                <p class="text-muted" style="max-width:460px; margin:0 auto 20px auto;">You currently do not have an active passenger ride in progress. Return to the Dashboard to accept new incoming ride requests.</p>
                <a href="{% url 'portal_rider' %}" class="btn text-white font-weight-bold px-4 py-2 rounded-pill shadow-sm" style="background:#f59e0b;">
                    <i class="fas fa-tachometer-alt mr-1"></i> Back to Rider Dashboard
                </a>
            </div>
            {% endif %}
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.min.js"></script>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        {% if active_ride %}
        var map = L.map('rider-map').setView([17.3850, 78.4867], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);
        L.marker([17.3850, 78.4867]).addTo(map).bindPopup("<b>Pickup:</b> {{ active_ride.pickup }}").openPopup();
        L.marker([17.4401, 78.3489]).addTo(map).bindPopup("<b>Drop:</b> {{ active_ride.drop }}");
        {% endif %}

        function updateDutyUI(isOnline) {
            const btn = document.getElementById('riderDutyToggleBtn');
            const text = document.getElementById('dutyBtnText');
            const dot = document.getElementById('dutyPulseDot');
            const ridesContainer = document.getElementById('riderRidesSection');
            const offDutyNotice = document.getElementById('riderOffDutyNotice');

            if (isOnline) {
                if (btn) { btn.style.background = '#10b981'; btn.style.borderColor = '#ffffff'; }
                if (text) text.innerText = 'ON DUTY';
                if (dot) dot.style.display = 'inline-block';
                if (ridesContainer) ridesContainer.style.display = 'block';
                if (offDutyNotice) offDutyNotice.style.display = 'none';
            } else {
                if (btn) { btn.style.background = '#ef4444'; btn.style.borderColor = '#ffffff'; }
                if (text) text.innerText = 'OFF DUTY';
                if (dot) dot.style.display = 'none';
                if (ridesContainer) ridesContainer.style.display = 'none';
                if (offDutyNotice) offDutyNotice.style.display = 'block';
            }
        }

        function toggleRiderDutyState() {
            let currentStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            let newStatus = (currentStatus === 'ON') ? 'OFF' : 'ON';
            localStorage.setItem('riderDutyStatus', newStatus);
            updateDutyUI(newStatus === 'ON');
        }

        document.addEventListener('DOMContentLoaded', function() {
            let savedStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            updateDutyUI(savedStatus === 'ON');
        });
    </script>
</body>
</html>"""

with open(os.path.join(templates_dir, "portal_rider_active.html"), "w", encoding="utf-8") as f:
    f.write(rider_active_html)

# 2. Update Rapido & Uber Captain features and Profile Save in portal_rider_profile.html
rider_profile_html = """{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Chauffeur Console - Captain Profile & Settings</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min-1.css'%}">
    <link rel="stylesheet" href="{% static 'css/premium_home.css' %}">
    <style>
        body { padding-top: 80px !important; font-family: 'Rubik', sans-serif; background-color: #fffbeb !important; color: #0f172a !important; }
        .live-dot { width:6px; height:6px; background:#ffffff; border-radius:50%; display:inline-block; }
        .premium-navbar { background-color:#f59e0b !important; border:none !important; box-shadow:0 4px 15px rgba(245,158,11,.3) !important; position:fixed !important; top:0; left:0; right:0; z-index:1030; padding:0 !important; }
        .premium-navbar .container-fluid { height:60px !important; padding:0 16px !important; display:flex !important; align-items:center !important; }
        .navbar-brand { color:#fff !important; font-size:1.15rem !important; font-weight:700 !important; display:flex !important; align-items:center !important; gap:8px; text-decoration:none !important; }
        .premium-navbar .nav-link { color:#fff !important; font-weight:500 !important; font-size:14px !important; padding:0 16px !important; height:60px !important; display:flex !important; align-items:center; text-decoration:none !important; transition:.25s; }
        .premium-navbar .nav-link:hover { background:rgba(255,255,255,.16) !important; }
        .premium-navbar .nav-link.active-nav { background:rgba(0,0,0,.12) !important; font-weight:700 !important; }

        /* Dynamic Dropdown Container */
        .premium-user-dropdown {
            min-width: 295px !important; border-radius: 16px !important; overflow: hidden !important; padding: 0 !important; margin-top: 8px !important;
            border: 1.5px solid rgba(245, 158, 11, 0.4) !important; box-shadow: 0 16px 45px rgba(245, 158, 11, 0.18), 0 4px 15px rgba(0,0,0,0.08) !important;
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px) !important;
        }
        .dropdown-section-label { font-size: 0.6rem !important; font-weight: 800 !important; letter-spacing: 0.8px !important; text-transform: uppercase !important; padding: 4px 14px 2px 14px !important; color: #d97706 !important; }
        .premium-dropdown-item { display: flex !important; align-items: center !important; justify-content: space-between !important; padding: 5px 10px !important; text-decoration: none !important; transition: all 0.2s ease !important; border-radius: 8px !important; margin: 1px 6px !important; width: calc(100% - 12px) !important; }
        .premium-dropdown-item:hover { transform: translateX(3px) !important; text-decoration: none !important; }
        .dropdown-icon-box { width: 28px !important; height: 28px !important; border-radius: 8px !important; display: flex !important; align-items: center !important; justify-content: center !important; font-size: 0.8rem !important; margin-right: 8px !important; }

        .item-colored-theme { background: rgba(245, 158, 11, 0.14) !important; }
        .item-colored-theme .dropdown-item-title { color: #d97706 !important; font-weight: 750 !important; }
        .item-colored-logout { background: rgba(239, 68, 68, 0.14) !important; }
        .item-colored-logout .dropdown-item-title { color: #dc2626 !important; font-weight: 750 !important; }
        .dropdown-item-title { font-size: 0.8rem !important; font-weight: 750 !important; color: #0f172a !important; margin-bottom: 0 !important; }
        .dropdown-item-sub { font-size: 0.65rem !important; color: #64748b !important; }
        .dropdown-divider-premium { height: 1px !important; margin: 3px 10px !important; background: rgba(226, 232, 240, 0.8) !important; }

        /* Amber, Black & White Only Palette */
        .profile-hero { background: linear-gradient(135deg, #f59e0b 0%, #d97706 60%, #b45309 100%); border-radius:24px; padding:32px; color:#fff; margin-bottom:24px; box-shadow:0 16px 48px rgba(245,158,11,.3); }
        .admin-avatar { width:84px; height:84px; border-radius:50%; background:rgba(255,255,255,.2); border:3px solid #fff; display:flex; align-items:center; justify-content:center; overflow:hidden; font-size:2.2rem; color:#fff; flex-shrink:0; }
        .admin-avatar img { width:100%; height:100%; object-fit:cover; }
        
        .captain-card { background:#ffffff; border-radius:20px; border:1.5px solid rgba(245,158,11,.25); border-top:4px solid #f59e0b; box-shadow:0 8px 24px rgba(15,23,42,.06); padding:24px; margin-bottom:24px; }
        .captain-title { font-size:1.05rem; font-weight:750; color:#0f172a; margin-bottom:18px; display:flex; align-items:center; justify-content:space-between; }
        
        .profile-input { border:1.5px solid rgba(245,158,11,.3); border-radius:10px; padding:10px 14px; font-size:.88rem; width:100%; color:#0f172a; font-weight:600; background:#fff; }
        .profile-input:focus { border-color:#f59e0b; outline:none; box-shadow:0 0 0 3px rgba(245,158,11,.15); }
        
        .img-upload-zone { border:2px dashed rgba(245,158,11,.4); border-radius:14px; background:#fffdf5; padding:20px; text-align:center; cursor:pointer; transition:all 0.25s; }
        .img-upload-zone:hover { border-color:#f59e0b; background:#fffbeb; }

        .toggle-switch { position:relative; display:inline-block; width:44px; height:24px; margin:0; }
        .toggle-switch input { opacity:0; width:0; height:0; }
        .toggle-slider { position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0; background:#cbd5e1; border-radius:24px; transition:.3s; }
        .toggle-slider:before { position:absolute; content:""; height:18px; width:18px; left:3px; bottom:3px; background:#fff; border-radius:50%; transition:.3s; box-shadow:0 2px 4px rgba(0,0,0,.15); }
        .toggle-switch input:checked + .toggle-slider { background:#f59e0b; }
        .toggle-switch input:checked + .toggle-slider:before { transform:translateX(20px); }

        .feature-row { display:flex; align-items:center; justify-content:space-between; padding:12px 0; border-bottom:1px solid rgba(245,158,11,.12); }
        .feature-row:last-child { border-bottom:none; }
    </style>
</head>
<body>
    <!-- Top Navbar -->
    <nav class="navbar navbar-expand-lg premium-navbar p-0">
        <div class="container-fluid">
            <div class="d-flex align-items-center">
                <a class="nav-menu-trigger dropdown-toggle mr-3" href="#" id="dashboardDropdown" data-toggle="dropdown" style="color: #fff;">
                    <i class="fas fa-bars"></i>
                </a>
                <div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; margin-top: 8px !important;">
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%) !important; padding: 10px 14px; color: #fff;">
                        <div class="d-flex align-items-center">
                            <div style="width:32px; height:32px; border-radius:10px; background:rgba(255,255,255,.22); display:flex; align-items:center; justify-content:center; margin-right:10px;">
                                {% if user_profile and user_profile.image %}
                                <img src="{{ user_profile.image.url }}" style="width:100%; height:100%; border-radius:10px; object-fit:cover;">
                                {% else %}
                                <i class="fas fa-motorcycle" style="font-size:14px; color:#fff;"></i>
                                {% endif %}
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold" style="font-size:0.82rem; color:#fff;">{{ user.get_full_name|default:user.username }}</h6>
                                <small class="text-white-50" style="font-size:0.65rem;">Rapido &amp; Uber Captain</small>
                            </div>
                        </div>
                        <span class="badge" style="background:rgba(255,255,255,.25); color:#fff; font-size:0.6rem; padding:3px 6px; border-radius:8px;">Active Rider</span>
                    </div>

                    <div class="py-1">
                        <div class="dropdown-section-label">Rider Profile &amp; Controls</div>
                        <a class="premium-dropdown-item item-colored-theme" href="{% url 'portal_rider_profile' %}">
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

                        <a class="premium-dropdown-item" href="{% url 'portal_rider_active' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(2,132,199,.14); color:#0284c7;"><i class="fas fa-motorcycle"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Active Rides</div>
                                    <div class="dropdown-item-sub">Live Trip Dashboard</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(2,132,199,.15); color:#0284c7; font-size:0.58rem; padding:2px 5px; border-radius:5px;">On Duty</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rider_trips' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(99,102,241,.14); color:#6366f1;"><i class="fas fa-history"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Ride History</div>
                                    <div class="dropdown-item-sub">Completed Trips Log</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(99,102,241,.12); color:#4f46e5; font-size:0.58rem; padding:2px 5px; border-radius:5px;">Logs</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rider_earnings' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(16,185,129,.14); color:#10b981;"><i class="fas fa-wallet"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Total Earnings</div>
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
                        <a class="premium-dropdown-item item-colored-logout" href="{% url 'portal_logout' %}">
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

                <a class="navbar-brand font-weight-bold" href="{% url 'portal_rider' %}">
                    <i class="fas fa-motorcycle mr-2"></i>Chauffeur Console
                </a>
            </div>

            <div class="d-flex align-items-center">
                <a class="nav-link" href="{% url 'portal_rider' %}"><i class="fas fa-tachometer-alt mr-1"></i> Dashboard</a>
                <a class="nav-link" href="{% url 'portal_rider_active' %}"><i class="fas fa-motorcycle mr-1"></i> Active Rides</a>
                <a class="nav-link" href="{% url 'portal_rider_trips' %}"><i class="fas fa-history mr-1"></i> Trips</a>
                <a class="nav-link" href="{% url 'portal_rider_earnings' %}"><i class="fas fa-wallet mr-1"></i> Earnings</a>
                <a class="nav-link active-nav" href="{% url 'portal_rider_profile' %}"><i class="fas fa-user-cog mr-1"></i> Profile &amp; Settings</a>
            </div>

            <!-- Compact Duty Toggle Button -->
            <div class="ml-auto d-flex align-items-center">
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-2 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1px solid #ffffff; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4); font-size: 0.72rem; display: inline-flex; align-items: center; gap: 4px; line-height: 1;">
                    <span id="dutyPulseDot" class="live-dot"></span>
                    <span id="dutyBtnText">ON DUTY</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container py-4">
        {% if messages %}
        {% for message in messages %}
        <div class="alert alert-warning alert-dismissible fade show rounded-lg shadow-sm mb-4" role="alert" style="background:#fff3cd; border-color:#ffebaa; color:#856404;">
            <i class="fas fa-check-circle mr-2"></i> {{ message }}
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        </div>
        {% endfor %}
        {% endif %}

        <!-- Hero Card -->
        <div class="profile-hero d-flex align-items-center justify-content-between flex-wrap" style="gap:20px;">
            <div class="d-flex align-items-center" style="gap:20px;">
                <div class="admin-avatar">
                    {% if user_profile and user_profile.image %}
                    <img src="{{ user_profile.image.url }}" alt="Rider Profile" id="heroProfileAvatar">
                    {% else %}
                    <i class="fas fa-user-ninja"></i>
                    {% endif %}
                </div>
                <div>
                    <h3 class="mb-1 font-weight-bold text-white" id="heroProfileName">{{ user.get_full_name|default:user.username }}</h3>
                    <p class="mb-2 text-white-50"><i class="fas fa-motorcycle mr-1"></i> Rapido &amp; Uber Captain Partner &bull; Zone: <span id="heroProfileLocation">{{ user_profile.location|default:'Central Hub' }}</span></p>
                    <div class="d-flex align-items-center flex-wrap" style="gap:10px;">
                        <span class="badge badge-light text-dark font-weight-bold"><i class="fas fa-star text-warning mr-1"></i> 4.95 Rating</span>
                        <span class="badge badge-light text-dark font-weight-bold"><i class="fas fa-phone text-dark mr-1"></i> <span id="heroProfilePhone">{{ user_profile.mobile_number|default:'+91 98765 43210' }}</span></span>
                        <span class="badge badge-light text-dark font-weight-bold"><i class="fas fa-check-circle text-success mr-1"></i> Helmet Verified</span>
                    </div>
                </div>
            </div>
            <div>
                <a href="{% url 'portal_rider_active' %}" class="btn btn-light text-dark font-weight-bold px-4 py-2 rounded-pill shadow-sm">
                    <i class="fas fa-motorcycle mr-1" style="color:#d97706;"></i> Go to Active Rides
                </a>
            </div>
        </div>

        <div class="row">
            <!-- LEFT COLUMN: Profile Details & Uber/Rapido Settings -->
            <div class="col-lg-8">
                
                <!-- 1. Profile & Avatar Image Form -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-user-edit mr-2" style="color:#d97706;"></i>Captain Profile &amp; Avatar Details</span>
                        <span class="badge badge-warning text-dark font-weight-bold">Rapido Verified</span>
                    </div>
                    <form method="POST" action="{% url 'portal_rider_profile' %}" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div class="form-group mb-4">
                            <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Driver Profile Image</label>
                            <div class="img-upload-zone" onclick="document.getElementById('profileImgInput').click();">
                                <div class="mb-2">
                                    {% if user_profile and user_profile.image %}
                                    <img src="{{ user_profile.image.url }}" id="imgPreview" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:2.5px solid #f59e0b;">
                                    {% else %}
                                    <div id="imgPreviewPlaceholder" style="width:70px; height:70px; border-radius:50%; background:rgba(245,158,11,.15); display:inline-flex; align-items:center; justify-content:center; color:#d97706; font-size:1.8rem;">
                                        <i class="fas fa-camera"></i>
                                    </div>
                                    <img src="" id="imgPreview" style="display:none; width:80px; height:80px; border-radius:50%; object-fit:cover; border:2.5px solid #f59e0b;">
                                    {% endif %}
                                </div>
                                <h6 class="mb-1 font-weight-bold" style="color:#d97706;">Click to Select / Upload New Profile Image</h6>
                                <small class="text-muted">Supports JPG, PNG, WEBP (Max 5MB)</small>
                                <input type="file" name="profile_image" id="profileImgInput" accept="image/*" onchange="previewImage(this);" style="display:none;">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Full Name</label>
                                <input type="text" name="full_name" class="profile-input" value="{{ user.get_full_name|default:user.username }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Email Address</label>
                                <input type="email" name="email" class="profile-input" value="{{ user.email }}">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Phone Number</label>
                                <input type="text" name="phone" class="profile-input" value="{{ user_profile.mobile_number|default:'+91 98765 43210' }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Operating Hub / City</label>
                                <input type="text" name="location" class="profile-input" value="{{ user_profile.location|default:'Central Hub' }}">
                            </div>
                        </div>

                        <button type="submit" class="btn text-white font-weight-bold px-4 py-2 rounded-pill mt-2 shadow-sm" style="background:#f59e0b; border:none;">
                            <i class="fas fa-save mr-1"></i> Save Captain Profile Changes
                        </button>
                    </form>
                </div>

                <!-- 2. Rapido & Uber Real-Time App Controls -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-sliders-h mr-2" style="color:#d97706;"></i>Rapido &amp; Uber Captain Dispatch Settings</span>
                        <span class="badge badge-dark">Live Sync</span>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">Auto-Accept Passenger Orders</div>
                            <small class="text-muted">Instantly accept incoming rides within operating radius</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Auto-Accept Rides setting updated')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">My Way Home Direction Filter</div>
                            <small class="text-muted">Only receive trips heading towards home destination</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" onchange="showToast('Home Direction Filter toggled')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">Surge Fare Loud Horn Alert</div>
                            <small class="text-muted">Play loud sound alert on high demand surge pricing</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Surge Alert Sound active')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">Toll &amp; Fuel Auto Reimbursement</div>
                            <small class="text-muted">Automatically add highway tolls to trip invoice</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Toll Reimbursement active')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">Driver Fatigue Rest Alert</div>
                            <small class="text-muted">Remind rest brake after 4 continuous driving hours</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Fatigue Alert active')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="mt-3 pt-3 border-top">
                        <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Fleet Ride Type Mode</label>
                        <select class="profile-input" onchange="showToast('Fleet Mode set to ' + this.value)">
                            <option value="Rapido 2-Wheeler Bike Taxi" selected>Rapido 2-Wheeler Bike Taxi</option>
                            <option value="Rapido 3-Wheeler Auto">Rapido 3-Wheeler Auto</option>
                            <option value="UberX Swift Sedan">UberX Swift Sedan</option>
                            <option value="Parcel Express Delivery">Parcel Express Delivery</option>
                        </select>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: Safety & Payout Setup -->
            <div class="col-lg-4">
                
                <!-- Compliance Card -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-shield-alt mr-2" style="color:#d97706;"></i>Safety &amp; Compliance Audit</span>
                        <span class="badge badge-warning text-dark font-weight-bold">Passed</span>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.85rem;">Driving License (DL)</div>
                            <small class="text-muted">Valid till Dec 2028</small>
                        </div>
                        <span class="badge badge-dark">Valid</span>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.85rem;">Vehicle RC &amp; Insurance</div>
                            <small class="text-muted">Fully Insured</small>
                        </div>
                        <span class="badge badge-dark">Active</span>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.85rem;">Helmet Inspection</div>
                            <small class="text-muted">Dual Helmets Passed</small>
                        </div>
                        <span class="badge badge-warning text-dark font-weight-bold">100% Pass</span>
                    </div>

                    <div class="mt-3 pt-2">
                        <button onclick="showToast('Emergency SOS Hotline Connected to Control Room')" class="btn btn-block btn-dark font-weight-bold py-2 rounded-pill">
                            <i class="fas fa-exclamation-triangle text-warning mr-1"></i> Emergency SOS Hotline
                        </button>
                    </div>
                </div>

                <!-- Payout Card -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-wallet mr-2" style="color:#d97706;"></i>Payout &amp; UPI Setup</span>
                    </div>

                    <div class="mb-3">
                        <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Instant UPI Auto-Credit ID</label>
                        <input type="text" class="profile-input mb-2" value="captain.rider@okaxis">
                        <small class="text-muted">Daily trip settlements auto-credited at 11:59 PM</small>
                    </div>

                    <div class="feature-row pt-2">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.85rem;">Instant Bank Payout</div>
                            <small class="text-muted">Transfer anytime to bank</small>
                        </div>
                        <button onclick="showToast('Instant Payout of ₹' + {{ total_earnings|default:250 }} + ' initiated')" class="btn btn-sm btn-warning text-dark font-weight-bold px-3 rounded-pill" style="background:#f59e0b; border:none;">
                            Withdraw
                        </button>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.min.js"></script>
    <script>
        function previewImage(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    $('#imgPreview').attr('src', e.target.result).show();
                    $('#imgPreviewPlaceholder').hide();
                    $('#heroProfileAvatar').attr('src', e.target.result);
                }
                reader.readAsDataURL(input.files[0]);
            }
        }

        function showToast(msg) {
            let t = document.createElement('div');
            t.style.cssText = 'position:fixed;bottom:24px;right:24px;background:#0f172a;color:#fff;padding:12px 20px;border-radius:12px;font-size:14px;z-index:9999;box-shadow:0 8px 20px rgba(0,0,0,0.3);border:1px solid #f59e0b;font-weight:600;';
            t.innerText = msg;
            document.body.appendChild(t);
            setTimeout(() => t.remove(), 3000);
        }

        function updateDutyUI(isOnline) {
            const btn = document.getElementById('riderDutyToggleBtn');
            const text = document.getElementById('dutyBtnText');
            const dot = document.getElementById('dutyPulseDot');

            if (isOnline) {
                if (btn) { btn.style.background = '#10b981'; btn.style.borderColor = '#ffffff'; }
                if (text) text.innerText = 'ON DUTY';
                if (dot) dot.style.display = 'inline-block';
            } else {
                if (btn) { btn.style.background = '#ef4444'; btn.style.borderColor = '#ffffff'; }
                if (text) text.innerText = 'OFF DUTY';
                if (dot) dot.style.display = 'none';
            }
        }

        function toggleRiderDutyState() {
            let currentStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            let newStatus = (currentStatus === 'ON') ? 'OFF' : 'ON';
            localStorage.setItem('riderDutyStatus', newStatus);
            updateDutyUI(newStatus === 'ON');
            showToast('Rider Status: ' + (newStatus === 'ON' ? 'ON DUTY' : 'OFF DUTY'));
        }

        document.addEventListener('DOMContentLoaded', function() {
            let savedStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            updateDutyUI(savedStatus === 'ON');
        });
    </script>
</body>
</html>"""

with open(os.path.join(templates_dir, "portal_rider_profile.html"), "w", encoding="utf-8") as f:
    f.write(rider_profile_html)

# 3. Update navbar duty toggle to compact size across all rider templates
rider_templates = [
    'portal_rider.html',
    'portal_rider_earnings.html',
    'portal_rider_trips.html'
]

compact_duty_btn = """            <!-- Compact Duty Toggle Button -->
            <div class="ml-auto d-flex align-items-center">
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-2 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1px solid #ffffff; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4); font-size: 0.72rem; display: inline-flex; align-items: center; gap: 4px; line-height: 1;">
                    <span id="dutyPulseDot" class="live-dot" style="width: 6px; height: 6px; background-color: #ffffff;"></span>
                    <span id="dutyBtnText">ON DUTY</span>
                </button>
            </div>"""

duty_js_global = """
    <script>
        function updateDutyUI(isOnline) {
            const btn = document.getElementById('riderDutyToggleBtn');
            const text = document.getElementById('dutyBtnText');
            const dot = document.getElementById('dutyPulseDot');
            const ridesContainer = document.getElementById('riderRidesSection');
            const offDutyNotice = document.getElementById('riderOffDutyNotice');

            if (isOnline) {
                if (btn) { btn.style.background = '#10b981'; btn.style.borderColor = '#ffffff'; }
                if (text) text.innerText = 'ON DUTY';
                if (dot) dot.style.display = 'inline-block';
                if (ridesContainer) ridesContainer.style.display = 'block';
                if (offDutyNotice) offDutyNotice.style.display = 'none';
            } else {
                if (btn) { btn.style.background = '#ef4444'; btn.style.borderColor = '#ffffff'; }
                if (text) text.innerText = 'OFF DUTY';
                if (dot) dot.style.display = 'none';
                if (ridesContainer) ridesContainer.style.display = 'none';
                if (offDutyNotice) offDutyNotice.style.display = 'block';
            }
        }

        function toggleRiderDutyState() {
            let currentStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            let newStatus = (currentStatus === 'ON') ? 'OFF' : 'ON';
            localStorage.setItem('riderDutyStatus', newStatus);
            updateDutyUI(newStatus === 'ON');
            if (typeof showToast === 'function') {
                showToast('Rider Status: ' + (newStatus === 'ON' ? 'ON DUTY' : 'OFF DUTY'));
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            let savedStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            updateDutyUI(savedStatus === 'ON');
        });
    </script>
"""

for fname in rider_templates:
    fpath = os.path.join(templates_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update button to compact duty button
        if 'id="riderDutyToggleBtn"' in content:
            start_btn = content.find('<!-- Duty Toggle Button on Far Right Corner -->')
            if start_btn == -1:
                start_btn = content.find('<div class="ml-auto d-flex align-items-center">\n                <button id="riderDutyToggleBtn"')
            if start_btn != -1:
                end_btn = content.find('</div>', start_btn)
                if end_btn != -1:
                    content = content[:start_btn] + compact_duty_btn + content[end_btn+6:]
        else:
            nav_end = content.find('</nav>')
            if nav_end != -1:
                content = content[:nav_end] + compact_duty_btn + "\n" + content[nav_end:]

        # Ensure duty_js_global is present before </body>
        if 'toggleRiderDutyState' not in content:
            body_end = content.find('</body>')
            if body_end != -1:
                content = content[:body_end] + duty_js_global + "\n" + content[body_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Active Ride Ticket page fixed, Rapido/Uber settings added, and compact global Duty toggle applied successfully!")
