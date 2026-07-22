import os

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

# 1. New portal_rider_profile.html with Rapido Captain features & Amber/Black/White theme only
rider_profile_code = """{% load static %}
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
        .live-dot { width:8px; height:8px; background:#10b981; border-radius:50%; display:inline-block; }
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

        /* Only Profile & Settings and Logout Colored */
        .item-colored-theme { background: rgba(245, 158, 11, 0.14) !important; }
        .item-colored-theme .dropdown-item-title { color: #d97706 !important; font-weight: 750 !important; }
        .item-colored-logout { background: rgba(239, 68, 68, 0.14) !important; }
        .item-colored-logout .dropdown-item-title { color: #dc2626 !important; font-weight: 750 !important; }
        .dropdown-item-title { font-size: 0.8rem !important; font-weight: 750 !important; color: #0f172a !important; margin-bottom: 0 !important; }
        .dropdown-item-sub { font-size: 0.65rem !important; color: #64748b !important; }
        .dropdown-divider-premium { height: 1px !important; margin: 3px 10px !important; background: rgba(226, 232, 240, 0.8) !important; }

        /* Amber, Black & White Only Cards */
        .profile-hero { background: linear-gradient(135deg, #f59e0b 0%, #d97706 60%, #b45309 100%); border-radius:24px; padding:32px; color:#fff; margin-bottom:24px; box-shadow:0 16px 48px rgba(245,158,11,.3); }
        .admin-avatar { width:84px; height:84px; border-radius:50%; background:rgba(255,255,255,.2); border:3px solid #fff; display:flex; align-items:center; justify-content:center; overflow:hidden; font-size:2.2rem; color:#fff; flex-shrink:0; }
        .admin-avatar img { width:100%; height:100%; object-fit:cover; }
        
        .captain-card { background:#ffffff; border-radius:20px; border:1.5px solid rgba(245,158,11,.25); border-top:4px solid #f59e0b; box-shadow:0 8px 24px rgba(15,23,42,.06); padding:24px; margin-bottom:24px; }
        .captain-title { font-size:1.05rem; font-weight:750; color:#0f172a; margin-bottom:18px; display:flex; align-items:center; justify-content:space-between; }
        
        .profile-input { border:1.5px solid rgba(245,158,11,.3); border-radius:10px; padding:10px 14px; font-size:.88rem; width:100%; color:#0f172a; font-weight:600; background:#fff; }
        .profile-input:focus { border-color:#f59e0b; outline:none; box-shadow:0 0 0 3px rgba(245,158,11,.15); }
        
        .img-upload-zone { border:2px dashed rgba(245,158,11,.4); border-radius:14px; background:#fffdf5; padding:20px; text-align:center; cursor:pointer; transition:all 0.25s; }
        .img-upload-zone:hover { border-color:#f59e0b; background:#fffbeb; }

        /* Toggle Switches */
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
                <a class="nav-link" href="{% url 'portal_rider_active' %}"><i class="fas fa-motorcycle mr-1"></i> Active Rides</a>
                <a class="nav-link" href="{% url 'portal_rider_trips' %}"><i class="fas fa-history mr-1"></i> Trips</a>
                <a class="nav-link" href="{% url 'portal_rider_earnings' %}"><i class="fas fa-wallet mr-1"></i> Earnings</a>
                <a class="nav-link active-nav" href="{% url 'portal_rider_profile' %}"><i class="fas fa-user-cog mr-1"></i> Profile &amp; Settings</a>
            </div>

            <!-- Duty Toggle Button on Far Right Corner -->
            <div class="ml-auto d-flex align-items-center">
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-3 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1.5px solid #ffffff; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4); transition: all 0.3s ease; font-size: 0.82rem; display: flex; align-items: center; gap: 6px;">
                    <span id="dutyPulseDot" class="live-dot" style="background-color: #ffffff;"></span>
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
                    <img src="{{ user_profile.image.url }}" alt="Rider Profile">
                    {% else %}
                    <i class="fas fa-user-ninja"></i>
                    {% endif %}
                </div>
                <div>
                    <h3 class="mb-1 font-weight-bold text-white">{{ user.get_full_name|default:user.username }}</h3>
                    <p class="mb-2 text-white-50"><i class="fas fa-motorcycle mr-1"></i> Rapido Captain Partner &bull; Verified Driver ID #CAP-8849</p>
                    <div class="d-flex align-items-center flex-wrap" style="gap:10px;">
                        <span class="badge badge-light text-dark font-weight-bold"><i class="fas fa-star text-warning mr-1"></i> 4.95 Captain Rating</span>
                        <span class="badge badge-light text-dark font-weight-bold"><i class="fas fa-check-circle text-success mr-1"></i> Helmet Inspected</span>
                    </div>
                </div>
            </div>
            <div>
                <a href="{% url 'portal_rider_active' %}" class="btn btn-light text-dark font-weight-bold px-4 py-2 rounded-pill shadow-sm">
                    <i class="fas fa-motorcycle mr-1" style="color:#d97706;"></i> Live Ride Dispatch
                </a>
            </div>
        </div>

        <div class="row">
            <!-- LEFT COLUMN: Profile Info & Rapido Captain Dispatch Settings -->
            <div class="col-lg-8">
                
                <!-- 1. Profile & Avatar Image Form -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-user-edit mr-2" style="color:#d97706;"></i>Captain Details &amp; Profile Picture</span>
                        <span class="badge badge-warning text-dark font-weight-bold">Captain Badge</span>
                    </div>
                    <form method="POST" action="{% url 'portal_rider_profile' %}" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div class="form-group mb-4">
                            <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Driver Photo Field</label>
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
                                <h6 class="mb-1 font-weight-bold" style="color:#d97706;">Upload Profile / Driver Avatar Image</h6>
                                <small class="text-muted">JPG, PNG, WEBP (Max 5MB)</small>
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
                                <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Contact Number</label>
                                <input type="text" name="phone" class="profile-input" value="{{ user_profile.mobile_number|default:'+91 98765 43210' }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Primary City / Zone</label>
                                <input type="text" name="location" class="profile-input" value="{{ user_profile.location|default:'Central Metro Zone' }}">
                            </div>
                        </div>

                        <button type="submit" class="btn text-white font-weight-bold px-4 py-2 rounded-pill mt-2 shadow-sm" style="background:#f59e0b; border:none;">
                            <i class="fas fa-save mr-1"></i> Update Captain Details
                        </button>
                    </form>
                </div>

                <!-- 2. Rapido Captain App Operating Mode Settings -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-sliders-h mr-2" style="color:#d97706;"></i>Rapido Captain Operating Controls</span>
                        <span class="badge badge-dark">App Version 4.8.2</span>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">Auto-Accept Nearby Rides</div>
                            <small class="text-muted">Automatically accept passenger requests within your radius</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Auto-Accept Rides setting saved')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">High Demand Surge Sound Alert</div>
                            <small class="text-muted">Play loud horn notification on high fare surge requests</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Surge Sound Alert enabled')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="feature-row">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.9rem;">Night Duty Bonus Mode (10 PM - 5 AM)</div>
                            <small class="text-muted">Enable +20% extra surge bonus for late night orders</small>
                        </div>
                        <label class="toggle-switch">
                            <input type="checkbox" checked onchange="showToast('Night Duty Bonus active')">
                            <span class="toggle-slider"></span>
                        </label>
                    </div>

                    <div class="mt-3 pt-3 border-top">
                        <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Preferred Dispatch Radius</label>
                        <select class="profile-input" onchange="showToast('Order radius set to ' + this.value)">
                            <option value="3 km">3 km Radius (Short Rides)</option>
                            <option value="5 km" selected>5 km Radius (Recommended)</option>
                            <option value="10 km">10 km Radius (Long Distance)</option>
                            <option value="Entire City">Entire Metro Area</option>
                        </select>
                    </div>
                </div>

            </div>

            <!-- RIGHT COLUMN: Vehicle Audit & Payout Preferences -->
            <div class="col-lg-4">
                
                <!-- Vehicle & License Verification Card -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-shield-alt mr-2" style="color:#d97706;"></i>Safety &amp; Compliance</span>
                        <span class="badge badge-warning text-dark font-weight-bold">Verified</span>
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
                            <small class="text-muted">Verified &amp; Insured</small>
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
                        <button onclick="showToast('Emergency SOS System Operational')" class="btn btn-block btn-dark font-weight-bold py-2 rounded-pill">
                            <i class="fas fa-exclamation-triangle text-warning mr-1"></i> Emergency SOS Hotline
                        </button>
                    </div>
                </div>

                <!-- Payout Preferences Card -->
                <div class="captain-card">
                    <div class="captain-title">
                        <span><i class="fas fa-wallet mr-2" style="color:#d97706;"></i>Captain Payout Setup</span>
                    </div>

                    <div class="mb-3">
                        <label class="font-weight-bold" style="font-size:0.85rem; color:#0f172a;">Instant UPI Handle</label>
                        <input type="text" class="profile-input mb-2" value="captain.rider@okaxis">
                        <small class="text-muted">Daily earnings automatically transferred at 11:59 PM</small>
                    </div>

                    <div class="feature-row pt-2">
                        <div>
                            <div class="font-weight-bold" style="color:#0f172a; font-size:0.85rem;">Instant Withdrawal</div>
                            <small class="text-muted">Withdraw earnings anytime</small>
                        </div>
                        <button onclick="showToast('Payout of ₹' + {{ total_earnings|default:250 }} + ' initiated')" class="btn btn-sm btn-warning text-dark font-weight-bold px-3 rounded-pill" style="background:#f59e0b; border:none;">
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
                btn.style.background = '#10b981';
                btn.style.boxShadow = '0 4px 12px rgba(16, 185, 129, 0.4)';
                text.innerText = 'ON DUTY';
                dot.style.display = 'inline-block';
            } else {
                btn.style.background = '#ef4444';
                btn.style.boxShadow = '0 4px 12px rgba(239, 68, 68, 0.4)';
                text.innerText = 'OFF DUTY';
                dot.style.display = 'none';
            }
        }

        function toggleRiderDutyState() {
            let currentStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            let newStatus = (currentStatus === 'ON') ? 'OFF' : 'ON';
            localStorage.setItem('riderDutyStatus', newStatus);
            updateDutyUI(newStatus === 'ON');
            showToast('Rider Status updated to ' + (newStatus === 'ON' ? 'ON DUTY' : 'OFF DUTY'));
        }

        document.addEventListener('DOMContentLoaded', function() {
            let savedStatus = localStorage.getItem('riderDutyStatus') || 'ON';
            updateDutyUI(savedStatus === 'ON');
        });
    </script>
</body>
</html>"""

with open(os.path.join(templates_dir, "portal_rider_profile.html"), "w", encoding="utf-8") as f:
    f.write(rider_profile_code)

# 2. Update navbar and Duty Toggle logic across all rider templates
rider_templates = [
    'portal_rider.html',
    'portal_rider_active.html',
    'portal_rider_earnings.html',
    'portal_rider_trips.html'
]

duty_btn_navbar_snippet = """            <!-- Duty Toggle Button on Far Right Corner -->
            <div class="ml-auto d-flex align-items-center">
                <button id="riderDutyToggleBtn" onclick="toggleRiderDutyState()" class="btn btn-sm font-weight-bold px-3 py-1 rounded-pill" style="background: #10b981; color: #ffffff; border: 1.5px solid #ffffff; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4); transition: all 0.3s ease; font-size: 0.82rem; display: flex; align-items: center; gap: 6px;">
                    <span id="dutyPulseDot" class="live-dot" style="background-color: #ffffff;"></span>
                    <span id="dutyBtnText">ON DUTY</span>
                </button>
            </div>"""

duty_js_snippet = """
    <script>
        function updateDutyUI(isOnline) {
            const btn = document.getElementById('riderDutyToggleBtn');
            const text = document.getElementById('dutyBtnText');
            const dot = document.getElementById('dutyPulseDot');
            const ridesContainer = document.getElementById('riderRidesSection');
            const offDutyNotice = document.getElementById('riderOffDutyNotice');

            if (isOnline) {
                if (btn) {
                    btn.style.background = '#10b981';
                    btn.style.boxShadow = '0 4px 12px rgba(16, 185, 129, 0.4)';
                }
                if (text) text.innerText = 'ON DUTY';
                if (dot) dot.style.display = 'inline-block';
                if (ridesContainer) ridesContainer.style.display = 'block';
                if (offDutyNotice) offDutyNotice.style.display = 'none';
            } else {
                if (btn) {
                    btn.style.background = '#ef4444';
                    btn.style.boxShadow = '0 4px 12px rgba(239, 68, 68, 0.4)';
                }
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
                showToast('Rider Status updated to ' + (newStatus === 'ON' ? 'ON DUTY' : 'OFF DUTY'));
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

        # Remove old static duty badge in brand if present
        content = content.replace('<span class="badge ml-2" style="font-size: 0.68rem; padding: 4px 9px; border-radius: 12px; background: rgba(255,255,255,0.22); color: #ffffff; border: 1px solid rgba(255,255,255,0.4);"><span class="live-dot mr-1" style="background-color: #ffffff;"></span>Rider Duty On</span>', '')

        # Insert duty button right after <div class="collapse navbar-collapse" ...> ... </div>
        if 'id="riderDutyToggleBtn"' not in content:
            nav_end = content.find('</nav>')
            if nav_end != -1:
                content = content[:nav_end] + duty_btn_navbar_snippet + "\n" + content[nav_end:]

        # Inject duty JS snippet before </body>
        if 'toggleRiderDutyState' not in content:
            body_end = content.find('</body>')
            if body_end != -1:
                content = content[:body_end] + duty_js_snippet + "\n" + content[body_end:]

        # In portal_rider.html, wrap dispatch feed in riderRidesSection and add riderOffDutyNotice
        if fname == 'portal_rider.html':
            if 'id="riderRidesSection"' not in content:
                content = content.replace('<div class="col-lg-5 mb-4">', '<div class="col-lg-5 mb-4">\n                <div id="riderOffDutyNotice" class="text-center py-5 my-4 bg-white rounded-xl shadow-sm border" style="display: none; border-color: rgba(239, 68, 68, 0.3) !important;">\n                    <div style="width: 70px; height: 70px; border-radius: 50%; background: rgba(239, 68, 68, 0.1); color: #ef4444; display: inline-flex; align-items: center; justify-content: center; font-size: 2rem; margin-bottom: 16px;">\n                        <i class="fas fa-power-off"></i>\n                    </div>\n                    <h4 class="font-weight-bold" style="color: #0f172a;">You Are Currently OFF DUTY</h4>\n                    <p class="text-muted" style="max-width: 480px; margin: 0 auto 20px auto; font-size: 0.9rem;">You will not receive any passenger booking requests or dispatch notifications until you switch your status back to <strong>ON DUTY</strong> in the navbar.</p>\n                    <button onclick="toggleRiderDutyState()" class="btn font-weight-bold px-4 py-2 rounded-pill shadow-sm" style="background: #10b981; color: #fff; border: none;">\n                        <i class="fas fa-toggle-on mr-2"></i> Switch ON DUTY Now\n                    </button>\n                </div>\n                <div id="riderRidesSection">')
                content = content.replace('<!-- RIGHT: Live Dispatch Feed -->', '<!-- RIGHT: Live Dispatch Feed -->')
                # Find end of col-lg-5
                end_col = content.find('</div>\n        </div>\n    </div>\n\n    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js">')
                if end_col != -1:
                    content = content[:end_col] + '</div>\n' + content[end_col:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname} with Duty Toggle Button and logic")

print("All Rider Duty Toggle updates & Rapido Captain Profile features successfully applied!")
