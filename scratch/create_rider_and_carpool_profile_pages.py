import os

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

# 1. Generate portal_rider_profile.html
rider_profile_html = """{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Chauffeur Console - Profile & Settings</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min-1.css'%}">
    <link rel="stylesheet" href="{% static 'css/premium_home.css' %}">
    <style>
        body { padding-top: 80px !important; font-family: 'Rubik', sans-serif; background-color: #fffbeb !important; color: #0f172a !important; }
        .live-dot { width:8px; height:8px; background:#f59e0b; border-radius:50%; display:inline-block; }
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

        .profile-hero { background: linear-gradient(135deg, #f59e0b 0%, #d97706 60%, #b45309 100%); border-radius:24px; padding:36px; color:#fff; margin-bottom:24px; box-shadow:0 16px 48px rgba(245,158,11,.3); }
        .admin-avatar { width:90px; height:90px; border-radius:50%; background:rgba(255,255,255,.2); border:3px solid #fff; display:flex; align-items:center; justify-content:center; overflow:hidden; font-size:2.2rem; color:#fff; flex-shrink:0; }
        .admin-avatar img { width:100%; height:100%; object-fit:cover; }
        .settings-card { background:#fff; border-radius:20px; border:1px solid rgba(245,158,11,.2); border-top:4px solid #f59e0b; box-shadow:0 6px 24px rgba(0,0,0,.06); padding:24px; margin-bottom:20px; }
        .profile-input { border:1.5px solid rgba(245,158,11,.3); border-radius:10px; padding:10px 14px; font-size:.9rem; width:100%; }
        .img-upload-zone { border:2px dashed rgba(245,158,11,.4); border-radius:14px; background:rgba(245,158,11,.03); padding:20px; text-align:center; cursor:pointer; }
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
                        <div class="dropdown-section-label">Rider Controls</div>
                        <a class="premium-dropdown-item item-colored-theme" href="{% url 'portal_rider_profile' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(245,158,11,.2); color:#d97706;"><i class="fas fa-user-cog"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Profile &amp; Settings</div>
                                    <div class="dropdown-item-sub">Rider Details &amp; Image</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(245,158,11,.15); color:#d97706; font-size:0.58rem; padding:2px 5px; border-radius:5px;"><i class="fas fa-shield-alt mr-1"></i>Verified</span>
                        </a>
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
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container py-4">
        {% if messages %}
        {% for message in messages %}
        <div class="alert alert-success alert-dismissible fade show rounded-lg shadow-sm mb-4" role="alert">
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
                    <p class="mb-2 text-white-50"><i class="fas fa-motorcycle mr-1"></i> Certified Chauffeur Partner &bull; Licensed Rider</p>
                    <div class="d-flex align-items-center flex-wrap" style="gap:10px;">
                        <span class="badge badge-light text-warning font-weight-bold"><i class="fas fa-star text-warning mr-1"></i> 4.9 Rating</span>
                        <span class="badge badge-light text-success font-weight-bold"><i class="fas fa-shield-alt text-success mr-1"></i> Verified Partner</span>
                    </div>
                </div>
            </div>
            <div>
                <a href="{% url 'portal_rider_active' %}" class="btn btn-light text-warning font-weight-bold px-4 py-2 rounded-pill shadow-sm">
                    <i class="fas fa-motorcycle mr-1"></i> Go to Live Rides
                </a>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-8">
                <!-- Profile & Vehicle Image Upload Form -->
                <div class="settings-card">
                    <h5 class="font-weight-bold mb-4" style="color:#d97706;"><i class="fas fa-user-edit mr-2"></i> Rider Profile Details &amp; Avatar Image</h5>
                    <form method="POST" action="{% url 'portal_rider_profile' %}" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div class="form-group mb-4">
                            <label class="font-weight-bold" style="font-size:0.88rem;">Profile Picture / Driver Photo</label>
                            <div class="img-upload-zone" onclick="document.getElementById('profileImgInput').click();">
                                <div class="mb-2">
                                    {% if user_profile and user_profile.image %}
                                    <img src="{{ user_profile.image.url }}" id="imgPreview" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:2px solid #f59e0b;">
                                    {% else %}
                                    <div id="imgPreviewPlaceholder" style="width:70px; height:70px; border-radius:50%; background:rgba(245,158,11,.15); display:inline-flex; align-items:center; justify-content:center; color:#d97706; font-size:1.8rem;">
                                        <i class="fas fa-camera"></i>
                                    </div>
                                    <img src="" id="imgPreview" style="display:none; width:80px; height:80px; border-radius:50%; object-fit:cover; border:2px solid #f59e0b;">
                                    {% endif %}
                                </div>
                                <h6 class="mb-1 font-weight-bold" style="color:#d97706;">Click to Upload / Change Profile Image</h6>
                                <small class="text-muted">Supports JPG, PNG, WEBP (Max 5MB)</small>
                                <input type="file" name="profile_image" id="profileImgInput" accept="image/*" onchange="previewImage(this);">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Full Name</label>
                                <input type="text" name="full_name" class="profile-input" value="{{ user.get_full_name|default:user.username }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Email Address</label>
                                <input type="email" name="email" class="profile-input" value="{{ user.email }}">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Phone Number</label>
                                <input type="text" name="phone" class="profile-input" value="{{ user_profile.mobile_number|default:'+91 98765 43210' }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Operating Hub / City</label>
                                <input type="text" name="location" class="profile-input" value="{{ user_profile.location|default:'Central Hub' }}">
                            </div>
                        </div>

                        <button type="submit" class="btn btn-warning text-white font-weight-bold px-4 py-2 rounded-pill mt-3 shadow-sm" style="background:#f59e0b; border:none;">
                            <i class="fas fa-save mr-1"></i> Save Profile Details
                        </button>
                    </form>
                </div>
            </div>

            <div class="col-lg-4">
                <!-- Operational Telemetry Card -->
                <div class="settings-card">
                    <h5 class="font-weight-bold mb-4" style="color:#d97706;"><i class="fas fa-satellite-dish mr-2"></i> Real-Time Rider Telemetry</h5>
                    <div class="d-flex align-items-center justify-content-between py-2 border-bottom">
                        <span class="font-weight-bold" style="font-size:0.85rem;">Dispatch Network</span>
                        <span class="badge badge-success"><i class="fas fa-circle live-dot mr-1"></i> Connected</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-between py-2 border-bottom">
                        <span class="font-weight-bold" style="font-size:0.85rem;">Completed Trips</span>
                        <span class="font-weight-bold text-dark">{{ total_trips }} Trips</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-between py-2 border-bottom">
                        <span class="font-weight-bold" style="font-size:0.85rem;">Net Earnings</span>
                        <span class="font-weight-bold text-success">₹{{ total_earnings }}</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-between py-2">
                        <span class="font-weight-bold" style="font-size:0.85rem;">GPS Signal</span>
                        <span class="badge badge-warning text-dark font-weight-bold">Ultra 4ms</span>
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
    </script>
</body>
</html>"""

with open(os.path.join(templates_dir, "portal_rider_profile.html"), "w", encoding="utf-8") as f:
    f.write(rider_profile_html)

# 2. Generate portal_carpool_profile.html
carpool_profile_html = """{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Pooling Console - Profile & Settings</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min-1.css'%}">
    <link rel="stylesheet" href="{% static 'css/premium_home.css' %}">
    <style>
        body { padding-top: 80px !important; font-family: 'Rubik', sans-serif; background-color: #fdf2f8 !important; color: #0f172a !important; }
        .live-dot { width:8px; height:8px; background:#ec4899; border-radius:50%; display:inline-block; }
        .premium-navbar { background-color:#ec4899 !important; border:none !important; box-shadow:0 4px 15px rgba(236,72,153,.3) !important; position:fixed !important; top:0; left:0; right:0; z-index:1030; padding:0 !important; }
        .premium-navbar .container-fluid { height:60px !important; padding:0 16px !important; display:flex !important; align-items:center !important; }
        .navbar-brand { color:#fff !important; font-size:1.15rem !important; font-weight:700 !important; display:flex !important; align-items:center !important; gap:8px; text-decoration:none !important; }
        .premium-navbar .nav-link { color:#fff !important; font-weight:500 !important; font-size:14px !important; padding:0 16px !important; height:60px !important; display:flex !important; align-items:center; text-decoration:none !important; transition:.25s; }
        .premium-navbar .nav-link:hover { background:rgba(255,255,255,.16) !important; }
        .premium-navbar .nav-link.active-nav { background:rgba(0,0,0,.12) !important; font-weight:700 !important; }

        /* Dynamic Dropdown Container */
        .premium-user-dropdown {
            min-width: 295px !important; border-radius: 16px !important; overflow: hidden !important; padding: 0 !important; margin-top: 8px !important;
            border: 1.5px solid rgba(236, 72, 153, 0.4) !important; box-shadow: 0 16px 45px rgba(236, 72, 153, 0.18), 0 4px 15px rgba(0,0,0,0.08) !important;
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px) !important;
        }
        .dropdown-section-label { font-size: 0.6rem !important; font-weight: 800 !important; letter-spacing: 0.8px !important; text-transform: uppercase !important; padding: 4px 14px 2px 14px !important; color: #be185d !important; }
        .premium-dropdown-item { display: flex !important; align-items: center !important; justify-content: space-between !important; padding: 5px 10px !important; text-decoration: none !important; transition: all 0.2s ease !important; border-radius: 8px !important; margin: 1px 6px !important; width: calc(100% - 12px) !important; }
        .premium-dropdown-item:hover { transform: translateX(3px) !important; text-decoration: none !important; }
        .dropdown-icon-box { width: 28px !important; height: 28px !important; border-radius: 8px !important; display: flex !important; align-items: center !important; justify-content: center !important; font-size: 0.8rem !important; margin-right: 8px !important; }

        /* Only Profile & Settings and Logout Colored */
        .item-colored-theme { background: rgba(236, 72, 153, 0.14) !important; }
        .item-colored-theme .dropdown-item-title { color: #be185d !important; font-weight: 750 !important; }
        .item-colored-logout { background: rgba(239, 68, 68, 0.14) !important; }
        .item-colored-logout .dropdown-item-title { color: #dc2626 !important; font-weight: 750 !important; }
        .dropdown-item-title { font-size: 0.8rem !important; font-weight: 750 !important; color: #0f172a !important; margin-bottom: 0 !important; }
        .dropdown-item-sub { font-size: 0.65rem !important; color: #64748b !important; }
        .dropdown-divider-premium { height: 1px !important; margin: 3px 10px !important; background: rgba(226, 232, 240, 0.8) !important; }

        .profile-hero { background: linear-gradient(135deg, #ec4899 0%, #d946ef 60%, #a855f7 100%); border-radius:24px; padding:36px; color:#fff; margin-bottom:24px; box-shadow:0 16px 48px rgba(236,72,153,.3); }
        .admin-avatar { width:90px; height:90px; border-radius:50%; background:rgba(255,255,255,.2); border:3px solid #fff; display:flex; align-items:center; justify-content:center; overflow:hidden; font-size:2.2rem; color:#fff; flex-shrink:0; }
        .admin-avatar img { width:100%; height:100%; object-fit:cover; }
        .settings-card { background:#fff; border-radius:20px; border:1px solid rgba(236,72,153,.2); border-top:4px solid #ec4899; box-shadow:0 6px 24px rgba(0,0,0,.06); padding:24px; margin-bottom:20px; }
        .profile-input { border:1.5px solid rgba(236,72,153,.3); border-radius:10px; padding:10px 14px; font-size:.9rem; width:100%; }
        .img-upload-zone { border:2px dashed rgba(236,72,153,.4); border-radius:14px; background:rgba(236,72,153,.03); padding:20px; text-align:center; cursor:pointer; }
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
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #ec4899 0%, #d946ef 50%, #a855f7 100%) !important; padding: 10px 14px; color: #fff;">
                        <div class="d-flex align-items-center">
                            <div style="width:32px; height:32px; border-radius:10px; background:rgba(255,255,255,.22); display:flex; align-items:center; justify-content:center; margin-right:10px;">
                                <i class="fas fa-users" style="font-size:14px; color:#fff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold" style="font-size:0.82rem; color:#fff;">Pooling Console</h6>
                                <small class="text-white-50" style="font-size:0.65rem;">Shared Network</small>
                            </div>
                        </div>
                        <span class="badge" style="background:rgba(255,255,255,.25); color:#fff; font-size:0.6rem; padding:3px 6px; border-radius:8px;">Pool Host</span>
                    </div>

                    <div class="py-1">
                        <div class="dropdown-section-label">Pooling Controls</div>
                        <a class="premium-dropdown-item item-colored-theme" href="{% url 'portal_carpool_profile' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(236,72,153,.2); color:#be185d;"><i class="fas fa-user-cog"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Profile &amp; Settings</div>
                                    <div class="dropdown-item-sub">Host Profile &amp; Image</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(236,72,153,.15); color:#be185d; font-size:0.58rem; padding:2px 5px; border-radius:5px;"><i class="fas fa-shield-alt mr-1"></i>Verified Host</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_carpool_publish' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(244,63,94,.14); color:#f43f5e;"><i class="fas fa-plus-circle"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Publish New Ride</div>
                                    <div class="dropdown-item-sub">Create Shared Route</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(244,63,94,.12); color:#e11d48; font-size:0.58rem; padding:2px 5px; border-radius:5px;">New Route</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_carpool_itineraries' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(2,132,199,.14); color:#0284c7;"><i class="fas fa-route"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Pooled Itineraries</div>
                                    <div class="dropdown-item-sub">Scheduled Rides</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(2,132,199,.15); color:#0284c7; font-size:0.58rem; padding:2px 5px; border-radius:5px;">Live</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_carpool_bookings' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(99,102,241,.14); color:#6366f1;"><i class="fas fa-users"></i></div>
                                <div>
                                    <div class="dropdown-item-title">Booking Requests</div>
                                    <div class="dropdown-item-sub">Passenger Seat Claims</div>
                                </div>
                            </div>
                            <span class="badge" style="background:rgba(99,102,241,.12); color:#4f46e5; font-size:0.58rem; padding:2px 5px; border-radius:5px;">Claims</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="/">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background:rgba(245,158,11,.14); color:#f59e0b;"><i class="fas fa-exchange-alt"></i></div>
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

                <a class="navbar-brand font-weight-bold" href="{% url 'portal_carpool' %}">
                    <i class="fas fa-users mr-2"></i>Pooling Console
                </a>
            </div>

            <div class="d-flex align-items-center">
                <a class="nav-link" href="{% url 'portal_carpool' %}"><i class="fas fa-tachometer-alt mr-1"></i> Dashboard</a>
                <a class="nav-link" href="{% url 'portal_carpool_publish' %}"><i class="fas fa-plus-circle mr-1"></i> Publish Ride</a>
                <a class="nav-link" href="{% url 'portal_carpool_itineraries' %}"><i class="fas fa-route mr-1"></i> Itineraries</a>
                <a class="nav-link" href="{% url 'portal_carpool_bookings' %}"><i class="fas fa-book mr-1"></i> Seat Requests</a>
                <a class="nav-link active-nav" href="{% url 'portal_carpool_profile' %}"><i class="fas fa-user-cog mr-1"></i> Profile &amp; Settings</a>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container py-4">
        {% if messages %}
        {% for message in messages %}
        <div class="alert alert-success alert-dismissible fade show rounded-lg shadow-sm mb-4" role="alert">
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
                    <img src="{{ user_profile.image.url }}" alt="Host Profile">
                    {% else %}
                    <i class="fas fa-user-circle"></i>
                    {% endif %}
                </div>
                <div>
                    <h3 class="mb-1 font-weight-bold text-white">{{ user.get_full_name|default:user.username }}</h3>
                    <p class="mb-2 text-white-50"><i class="fas fa-route mr-1"></i> Certified Pooling Host &bull; Community Driver</p>
                    <div class="d-flex align-items-center flex-wrap" style="gap:10px;">
                        <span class="badge badge-light text-pink font-weight-bold" style="color:#be185d;"><i class="fas fa-star text-warning mr-1"></i> 5.0 Host Rating</span>
                        <span class="badge badge-light text-purple font-weight-bold" style="color:#7c3aed;"><i class="fas fa-shield-alt text-purple mr-1"></i> ID Verified</span>
                    </div>
                </div>
            </div>
            <div>
                <a href="{% url 'portal_carpool_publish' %}" class="btn btn-light font-weight-bold px-4 py-2 rounded-pill shadow-sm" style="color:#be185d;">
                    <i class="fas fa-plus-circle mr-1"></i> Publish New Route
                </a>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-8">
                <!-- Profile & Vehicle Image Upload Form -->
                <div class="settings-card">
                    <h5 class="font-weight-bold mb-4" style="color:#be185d;"><i class="fas fa-user-edit mr-2"></i> Host Profile Details &amp; Image</h5>
                    <form method="POST" action="{% url 'portal_carpool_profile' %}" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div class="form-group mb-4">
                            <label class="font-weight-bold" style="font-size:0.88rem;">Host Photo / Avatar Image</label>
                            <div class="img-upload-zone" onclick="document.getElementById('profileImgInput').click();">
                                <div class="mb-2">
                                    {% if user_profile and user_profile.image %}
                                    <img src="{{ user_profile.image.url }}" id="imgPreview" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:2px solid #ec4899;">
                                    {% else %}
                                    <div id="imgPreviewPlaceholder" style="width:70px; height:70px; border-radius:50%; background:rgba(236,72,153,.15); display:inline-flex; align-items:center; justify-content:center; color:#be185d; font-size:1.8rem;">
                                        <i class="fas fa-camera"></i>
                                    </div>
                                    <img src="" id="imgPreview" style="display:none; width:80px; height:80px; border-radius:50%; object-fit:cover; border:2px solid #ec4899;">
                                    {% endif %}
                                </div>
                                <h6 class="mb-1 font-weight-bold" style="color:#be185d;">Click to Upload / Change Profile Image</h6>
                                <small class="text-muted">Supports JPG, PNG, WEBP (Max 5MB)</small>
                                <input type="file" name="profile_image" id="profileImgInput" accept="image/*" onchange="previewImage(this);">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Full Name</label>
                                <input type="text" name="full_name" class="profile-input" value="{{ user.get_full_name|default:user.username }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Email Address</label>
                                <input type="email" name="email" class="profile-input" value="{{ user.email }}">
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Contact Mobile</label>
                                <input type="text" name="phone" class="profile-input" value="{{ user_profile.mobile_number|default:'+91 98765 43210' }}">
                            </div>
                            <div class="col-md-6 mb-3">
                                <label class="font-weight-bold" style="font-size:0.85rem;">Primary Commute Route</label>
                                <input type="text" name="location" class="profile-input" value="{{ user_profile.location|default:'City Express Corridor' }}">
                            </div>
                        </div>

                        <button type="submit" class="btn text-white font-weight-bold px-4 py-2 rounded-pill mt-3 shadow-sm" style="background:#ec4899; border:none;">
                            <i class="fas fa-save mr-1"></i> Save Host Profile
                        </button>
                    </form>
                </div>
            </div>

            <div class="col-lg-4">
                <!-- Operational Telemetry Card -->
                <div class="settings-card">
                    <h5 class="font-weight-bold mb-4" style="color:#be185d;"><i class="fas fa-satellite-dish mr-2"></i> Real-Time Host Telemetry</h5>
                    <div class="d-flex align-items-center justify-content-between py-2 border-bottom">
                        <span class="font-weight-bold" style="font-size:0.85rem;">Pool Network</span>
                        <span class="badge badge-success"><i class="fas fa-circle live-dot mr-1"></i> Active</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-between py-2 border-bottom">
                        <span class="font-weight-bold" style="font-size:0.85rem;">Published Routes</span>
                        <span class="font-weight-bold text-dark">{{ total_routes }} Routes</span>
                    </div>
                    <div class="d-flex align-items-center justify-content-between py-2">
                        <span class="font-weight-bold" style="font-size:0.85rem;">Sync Latency</span>
                        <span class="badge font-weight-bold" style="background:rgba(236,72,153,.15); color:#be185d;">Ultra 3ms</span>
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
    </script>
</body>
</html>"""

with open(os.path.join(templates_dir, "portal_carpool_profile.html"), "w", encoding="utf-8") as f:
    f.write(carpool_profile_html)

print("Created portal_rider_profile.html and portal_carpool_profile.html successfully!")
