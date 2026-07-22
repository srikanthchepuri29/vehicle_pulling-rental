import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', 'templates')

html = r"""{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Rental Console - Profile and Settings</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta name="description" content="Rental Admin Profile and Settings - manage account, security, and real-time fleet scenarios.">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.0/css/all.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min-1.css'%}">
    <link rel="stylesheet" href="{% static 'css/premium_home.css' %}">
    <style>
        @keyframes livePulseDot {
            0%  { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16,185,129,.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 8px rgba(16,185,129,0); }
            100%{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16,185,129,0); }
        }
        @keyframes avatarPulse {
            0%,100%{ box-shadow: 0 0 0 0 rgba(16,185,129,.4); }
            50%    { box-shadow: 0 0 0 14px rgba(16,185,129,0); }
        }
        @keyframes shimmerGreen {
            0%  { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100%{ background-position: 0% 50%; }
        }
        @keyframes slideUp {
            from{ opacity:0; transform:translateY(18px); }
            to  { opacity:1; transform:translateY(0); }
        }
        body { padding-top: 80px !important; font-family: 'Rubik', sans-serif; background-color: var(--body-bg, #f0fdf4) !important; color: var(--text-color, #0f172a) !important; }
        .live-dot { width:8px; height:8px; background:#10b981; border-radius:50%; display:inline-block; animation:livePulseDot 1.8s infinite; }
        /* Navbar */
        .premium-navbar { background-color:#10b981 !important; border:none !important; box-shadow:0 4px 15px rgba(16,185,129,.3) !important; position:fixed !important; top:0; left:0; right:0; z-index:1030; padding:0 !important; }
        .premium-navbar .container-fluid { height:60px !important; padding:0 16px !important; display:flex !important; align-items:center !important; }
        .navbar-brand { color:#fff !important; font-size:1.15rem !important; font-weight:700 !important; display:flex !important; align-items:center !important; padding:0 16px 0 0 !important; gap:8px; text-decoration:none !important; }
        .premium-navbar .nav-link { color:#fff !important; font-weight:500 !important; font-size:14px !important; padding:0 16px !important; height:60px !important; display:flex !important; align-items:center; text-decoration:none !important; transition:.25s; }
        .premium-navbar .nav-link:hover { background:rgba(255,255,255,.16) !important; }
        .premium-navbar .nav-link.active-nav { background:rgba(0,0,0,.12) !important; font-weight:700 !important; }
        /* Dropdown */
        .dropdown-item-green { color:#10b981 !important; background:transparent !important; border-radius:10px; padding:8px 14px; margin:3px 8px; display:flex; align-items:center; justify-content:space-between; text-decoration:none; transition:.25s; font-weight:600; font-size:.84rem; }
        .dropdown-item-green:hover { background:rgba(16,185,129,.12) !important; transform:translateX(4px); color:#047857 !important; text-decoration:none !important; }
        .dropdown-item-red { color:#ef4444 !important; background:transparent !important; border-radius:10px; padding:8px 14px; margin:3px 8px; display:flex; align-items:center; text-decoration:none; transition:.25s; font-weight:600; font-size:.84rem; }
        .dropdown-item-red:hover { background:rgba(239,68,68,.12) !important; transform:translateX(4px); text-decoration:none !important; }
        .dropdown-item-normal { color:var(--text-color,#1e293b) !important; background:transparent !important; border-radius:10px; padding:8px 14px; margin:3px 8px; display:flex; align-items:center; justify-content:space-between; text-decoration:none; transition:.25s; font-size:.84rem; font-weight:500; }
        .dropdown-item-normal:hover { background:rgba(16,185,129,.1) !important; color:#10b981 !important; transform:translateX(4px); text-decoration:none !important; }
        /* Profile Hero */
        .profile-hero {
            background: linear-gradient(135deg, #10b981 0%, #047857 60%, #065f46 100%);
            border-radius:24px; padding:40px 36px; position:relative; overflow:hidden;
            box-shadow:0 16px 48px rgba(16,185,129,.3); animation:slideUp .5s ease; margin-bottom:24px;
        }
        .profile-hero::before { content:''; position:absolute; top:-60px; right:-60px; width:260px; height:260px; background:rgba(255,255,255,.06); border-radius:50%; }
        .profile-hero::after  { content:''; position:absolute; bottom:-80px; left:40%; width:200px; height:200px; background:rgba(255,255,255,.04); border-radius:50%; }
        .admin-avatar {
            width:96px; height:96px; border-radius:50%;
            background:rgba(255,255,255,.2); border:3px solid rgba(255,255,255,.6);
            display:flex; align-items:center; justify-content:center;
            font-size:2.5rem; color:#fff; animation:avatarPulse 3s infinite;
            flex-shrink:0; position:relative; z-index:1;
        }
        .stat-pill {
            display:inline-flex; align-items:center; gap:6px;
            background:rgba(255,255,255,.18); border:1px solid rgba(255,255,255,.3);
            border-radius:20px; padding:5px 14px; font-size:.8rem; color:#fff; font-weight:600;
        }
        /* KPI Cards */
        .kpi-card {
            background:var(--card-bg,#fff); border-radius:16px;
            border:1px solid rgba(16,185,129,.15); box-shadow:0 4px 16px rgba(16,185,129,.07);
            padding:22px; text-align:center; transition:.3s; animation:slideUp .55s ease;
        }
        .kpi-card:hover { transform:translateY(-3px); box-shadow:0 8px 24px rgba(16,185,129,.14); }
        .kpi-icon { width:48px; height:48px; border-radius:14px; background:rgba(16,185,129,.12); display:inline-flex; align-items:center; justify-content:center; margin-bottom:10px; }
        /* Settings Cards */
        .settings-card {
            background:var(--card-bg,#fff); border-radius:20px;
            border:1px solid rgba(16,185,129,.15); border-top:4px solid #10b981;
            box-shadow:0 6px 24px rgba(16,185,129,.07); padding:28px;
            transition:.3s; animation:slideUp .6s ease;
        }
        .settings-card:hover { box-shadow:0 10px 32px rgba(16,185,129,.13); }
        .section-icon { width:36px; height:36px; border-radius:10px; background:rgba(16,185,129,.12); display:flex; align-items:center; justify-content:center; margin-right:12px; flex-shrink:0; }
        /* Toggle */
        .toggle-switch { position:relative; display:inline-block; width:48px; height:26px; }
        .toggle-switch input { opacity:0; width:0; height:0; }
        .toggle-slider { position:absolute; cursor:pointer; top:0; left:0; right:0; bottom:0; background:#cbd5e1; border-radius:26px; transition:.35s; }
        .toggle-slider:before { position:absolute; content:""; height:20px; width:20px; left:3px; bottom:3px; background:#fff; border-radius:50%; transition:.35s; box-shadow:0 2px 4px rgba(0,0,0,.15); }
        .toggle-switch input:checked + .toggle-slider { background:#10b981; }
        .toggle-switch input:checked + .toggle-slider:before { transform:translateX(22px); }
        /* Setting rows */
        .setting-row { display:flex; align-items:center; justify-content:space-between; padding:14px 0; border-bottom:1px solid rgba(16,185,129,.08); transition:.2s; }
        .setting-row:last-child { border-bottom:none; }
        .setting-row:hover { background:rgba(16,185,129,.03); border-radius:10px; padding-left:8px; padding-right:8px; }
        /* Security badges */
        .sec-badge { display:inline-flex; align-items:center; gap:5px; padding:3px 10px; border-radius:20px; font-size:.73rem; font-weight:700; }
        .sec-green { background:rgba(16,185,129,.12); color:#10b981; border:1px solid rgba(16,185,129,.3); }
        .sec-orange { background:rgba(245,158,11,.12); color:#d97706; border:1px solid rgba(245,158,11,.3); }
        /* Profile inputs */
        .profile-input { border:1.5px solid rgba(16,185,129,.25); border-radius:10px; padding:10px 14px; font-size:.9rem; background:var(--card-bg,#fff); color:var(--text-color,#1e293b); width:100%; transition:.2s; }
        .profile-input:focus { border-color:#10b981; outline:none; box-shadow:0 0 0 3px rgba(16,185,129,.1); }
    </style>
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg premium-navbar p-0">
    <div class="container-fluid d-flex align-items-center">
        <!-- Hamburger dropdown -->
        <div class="dropdown mr-2" style="align-self:center;">
            <a class="dropdown-toggle" href="#" id="dropMenu" role="button" data-toggle="dropdown" style="color:#fff; text-decoration:none;">
                <i class="fas fa-bars"></i>
            </a>
            <div class="dropdown-menu" aria-labelledby="dropMenu" style="position:absolute !important; left:0 !important; margin-top:8px !important; min-width:270px; z-index:1050; padding:0; overflow:hidden; border-radius:16px; border:1px solid rgba(16,185,129,.4); box-shadow:0 16px 45px rgba(16,185,129,.25); background:var(--card-bg,#fff) !important;">
                <div style="background:linear-gradient(135deg,#10b981 0%,#047857 100%); padding:14px 18px; display:flex; align-items:center;">
                    <div style="width:38px;height:38px;border-radius:12px;background:rgba(255,255,255,.22);display:flex;align-items:center;justify-content:center;margin-right:12px;">
                        <i class="fas fa-car-side" style="font-size:18px;color:#fff;"></i>
                    </div>
                    <h6 class="mb-0 font-weight-bold text-white" style="font-size:.9rem;">Rental Settings Console</h6>
                </div>
                <div class="py-2" style="background:var(--card-bg,#fff) !important;">
                    <ul style="list-style:none;padding:0;margin-bottom:2px;">
                        <li>
                            <a class="dropdown-item-green" href="{% url 'portal_rental_profile' %}">
                                <div class="d-flex align-items-center" style="gap:10px;">
                                    <div style="width:26px;height:26px;border-radius:6px;background:rgba(16,185,129,.12);display:flex;align-items:center;justify-content:center;">
                                        <i class="fas fa-user-cog" style="font-size:.8rem;color:#10b981;"></i>
                                    </div>
                                    <span>Profile &amp; Settings</span>
                                </div>
                                <i class="fas fa-chevron-right" style="font-size:.65rem;opacity:.6;"></i>
                            </a>
                        </li>
                    </ul>
                    <div style="height:1px;background:rgba(16,185,129,.15);margin:6px 10px;"></div>
                    <div class="px-3 py-1 font-weight-bold text-uppercase" style="font-size:.64rem;letter-spacing:.7px;color:#10b981;">Real-Time Fleet Controls</div>
                    <ul style="list-style:none;padding:0;margin-bottom:2px;">
                        <li>
                            <a class="dropdown-item-normal" href="{% url 'portal_rental_bookings' %}">
                                <div class="d-flex align-items-center" style="gap:10px;">
                                    <i class="fas fa-book" style="width:16px;color:#10b981 !important;"></i><span>Booking Requests</span>
                                </div>
                                <span class="badge" style="font-size:.65rem;padding:3px 8px;border-radius:10px;background:linear-gradient(135deg,#10b981,#047857);color:#fff;font-weight:700;">Live Log</span>
                            </a>
                        </li>
                        <li>
                            <a class="dropdown-item-normal" href="{% url 'portal_rental_remaining' %}">
                                <div class="d-flex align-items-center" style="gap:10px;">
                                    <i class="fas fa-clipboard-list" style="width:16px;color:#10b981 !important;"></i><span>Remaining Fleet</span>
                                </div>
                                <span class="badge" style="font-size:.65rem;padding:3px 8px;border-radius:10px;background:rgba(16,185,129,.15);color:#10b981;font-weight:700;">Active</span>
                            </a>
                        </li>
                        <li>
                            <a class="dropdown-item-normal" href="{% url 'portal_rental_completed' %}">
                                <div class="d-flex align-items-center" style="gap:10px;">
                                    <i class="fas fa-check-double" style="width:16px;color:#10b981 !important;"></i><span>Rides Completed</span>
                                </div>
                                <span class="badge" style="font-size:.65rem;padding:3px 8px;border-radius:10px;background:rgba(16,185,129,.15);color:#10b981;font-weight:700;">Done</span>
                            </a>
                        </li>
                    </ul>
                    <div style="height:1px;background:rgba(16,185,129,.15);margin:6px 10px;"></div>
                    <ul style="list-style:none;padding:0;margin-bottom:4px;">
                        <li>
                            <a class="dropdown-item-normal" href="{% url 'home' %}">
                                <div class="d-flex align-items-center" style="gap:10px;">
                                    <i class="fas fa-home text-muted" style="width:16px;"></i><span>Exit</span>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a class="dropdown-item-red" href="{% url 'portal_logout' %}">
                                <div class="d-flex align-items-center" style="gap:10px;">
                                    <i class="fas fa-sign-out-alt" style="width:16px;"></i><span>Logout</span>
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <a class="navbar-brand" href="{% url 'portal_rental' %}"><i class="fas fa-car mr-2"></i>Rental Console</a>
        <div class="collapse navbar-collapse" id="navContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item"><a class="nav-link" href="{% url 'portal_rental' %}"><i class="fas fa-home mr-1"></i> Portal Home</a></li>
                <li class="nav-item"><a class="nav-link" href="{% url 'portal_rental_bookings' %}"><i class="fas fa-book mr-1"></i> Bookings</a></li>
                <li class="nav-item"><a class="nav-link" href="{% url 'portal_rental_cars' %}"><i class="fas fa-car mr-1"></i> Fleet Catalog</a></li>
                <li class="nav-item"><a class="nav-link active-nav" href="{% url 'portal_rental_profile' %}"><i class="fas fa-user-cog mr-1"></i> Profile &amp; Settings</a></li>
            </ul>
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="{% url 'home' %}"><i class="fas fa-home mr-1"></i> Exit</a></li>
            </ul>
        </div>
    </div>
</nav>

<!-- MAIN -->
<div class="container-fluid px-4 py-4" style="max-width:1300px; margin:0 auto;">

    <!-- SECTION 1: Admin Profile Hero -->
    <div class="profile-hero">
        <div class="d-flex align-items-center flex-wrap" style="gap:24px; position:relative; z-index:1;">
            <div class="admin-avatar"><i class="fas fa-user-tie"></i></div>
            <div class="flex-grow-1">
                <div class="d-flex align-items-center flex-wrap mb-2" style="gap:10px;">
                    <h2 class="font-weight-bold text-white mb-0" style="font-size:1.6rem;">{{ user.get_full_name|default:user.username }}</h2>
                    <span class="stat-pill"><i class="fas fa-shield-alt mr-1"></i>Rental Admin</span>
                    <span class="stat-pill"><span class="live-dot mr-1" style="background:#fff;"></span>Online</span>
                </div>
                <div class="d-flex flex-wrap mb-3" style="gap:18px;">
                    <span class="text-white" style="opacity:.85;font-size:.88rem;"><i class="fas fa-envelope mr-2" style="opacity:.7;"></i>{{ user.email|default:"admin@rentalfleet.com" }}</span>
                    <span class="text-white" style="opacity:.85;font-size:.88rem;"><i class="fas fa-calendar-alt mr-2" style="opacity:.7;"></i>Joined: {{ user.date_joined|date:"M d, Y" }}</span>
                    <span class="text-white" style="opacity:.85;font-size:.88rem;"><i class="fas fa-clock mr-2" style="opacity:.7;"></i>Last Login: {{ user.last_login|date:"M d, Y H:i"|default:"Today" }}</span>
                </div>
                <div class="d-flex flex-wrap" style="gap:10px;">
                    <span class="stat-pill"><i class="fas fa-car mr-1"></i>{{ total_fleet }} Fleet Cars</span>
                    <span class="stat-pill"><i class="fas fa-book mr-1"></i>{{ total_bookings }} Total Bookings</span>
                    <span class="stat-pill"><i class="fas fa-rupee-sign mr-1"></i>&#8377;{{ total_revenue|floatformat:0 }} Revenue</span>
                    <span class="stat-pill"><i class="fas fa-check-double mr-1"></i>{{ completed_bookings }} Completed Rides</span>
                </div>
            </div>
            <div style="position:relative;z-index:1;">
                <button class="btn font-weight-bold px-4 py-2 rounded-pill" style="background:rgba(255,255,255,.2);border:1.5px solid rgba(255,255,255,.5);color:#fff;" onclick="document.getElementById('editSection').scrollIntoView({behavior:'smooth'});">
                    <i class="fas fa-edit mr-2"></i>Edit Profile
                </button>
            </div>
        </div>
    </div>

    <!-- SECTION 2: Fleet KPIs -->
    <div class="row mb-4">
        <div class="col-6 col-md-3 mb-3">
            <div class="kpi-card">
                <div class="kpi-icon"><i class="fas fa-car" style="color:#10b981;font-size:1.3rem;"></i></div>
                <h4 class="font-weight-bold mb-0" style="color:#10b981;">{{ total_fleet }}</h4>
                <small class="text-muted">Total Fleet</small>
            </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
            <div class="kpi-card">
                <div class="kpi-icon" style="background:rgba(245,158,11,.12);"><i class="fas fa-key" style="color:#f59e0b;font-size:1.3rem;"></i></div>
                <h4 class="font-weight-bold mb-0" style="color:#f59e0b;">{{ rented_count }}</h4>
                <small class="text-muted">Rented Out</small>
            </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
            <div class="kpi-card">
                <div class="kpi-icon" style="background:rgba(99,102,241,.12);"><i class="fas fa-check-double" style="color:#6366f1;font-size:1.3rem;"></i></div>
                <h4 class="font-weight-bold mb-0" style="color:#6366f1;">{{ completed_bookings }}</h4>
                <small class="text-muted">Completed Rides</small>
            </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
            <div class="kpi-card">
                <div class="kpi-icon" style="background:rgba(239,68,68,.1);"><i class="fas fa-hourglass-half" style="color:#ef4444;font-size:1.3rem;"></i></div>
                <h4 class="font-weight-bold mb-0" style="color:#ef4444;">{{ pending_bookings }}</h4>
                <small class="text-muted">Pending Approvals</small>
            </div>
        </div>
    </div>

    <div class="row">
        <!-- LEFT: Profile Details + Security -->
        <div class="col-lg-6 mb-4">

            <!-- Profile Details Card -->
            <div class="settings-card mb-4" id="editSection">
                <div class="d-flex align-items-center mb-4">
                    <div class="section-icon"><i class="fas fa-id-card" style="color:#10b981;font-size:.95rem;"></i></div>
                    <div>
                        <h5 class="font-weight-bold mb-0 text-title" style="font-size:1.05rem;">Admin Profile Details</h5>
                        <small class="text-muted">Your account identity and contact information</small>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label class="font-weight-bold text-muted d-block mb-1" style="font-size:.79rem;text-transform:uppercase;letter-spacing:.5px;">Full Name</label>
                        <input type="text" class="profile-input" value="{{ user.get_full_name|default:user.username }}">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="font-weight-bold text-muted d-block mb-1" style="font-size:.79rem;text-transform:uppercase;letter-spacing:.5px;">Username</label>
                        <input type="text" class="profile-input" value="{{ user.username }}" readonly style="background:rgba(16,185,129,.04);color:#64748b;">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="font-weight-bold text-muted d-block mb-1" style="font-size:.79rem;text-transform:uppercase;letter-spacing:.5px;">Email Address</label>
                        <input type="email" class="profile-input" value="{{ user.email|default:'admin@rentalfleet.com' }}">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="font-weight-bold text-muted d-block mb-1" style="font-size:.79rem;text-transform:uppercase;letter-spacing:.5px;">Role</label>
                        <input type="text" class="profile-input" value="Fleet Rental Administrator" readonly style="background:rgba(16,185,129,.04);color:#64748b;">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="font-weight-bold text-muted d-block mb-1" style="font-size:.79rem;text-transform:uppercase;letter-spacing:.5px;">Phone Number</label>
                        <input type="text" class="profile-input" placeholder="Enter phone number">
                    </div>
                    <div class="col-md-6 mb-3">
                        <label class="font-weight-bold text-muted d-block mb-1" style="font-size:.79rem;text-transform:uppercase;letter-spacing:.5px;">Location / Office</label>
                        <input type="text" class="profile-input" placeholder="City, State">
                    </div>
                </div>
                <div class="d-flex" style="gap:10px;margin-top:4px;">
                    <button type="button" class="btn text-white font-weight-bold px-4 py-2 rounded-pill save-btn" style="background:linear-gradient(135deg,#10b981,#047857);border:none;font-size:.88rem;">
                        <i class="fas fa-save mr-2"></i>Save Profile
                    </button>
                    <button type="button" class="btn font-weight-bold px-4 py-2 rounded-pill" style="background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.3);color:#10b981;font-size:.88rem;">
                        <i class="fas fa-sync-alt mr-2"></i>Reset
                    </button>
                </div>
            </div>

            <!-- Security Features Card -->
            <div class="settings-card" style="border-top-color:#6366f1;">
                <div class="d-flex align-items-center mb-4">
                    <div class="section-icon" style="background:rgba(99,102,241,.12);"><i class="fas fa-shield-alt" style="color:#6366f1;font-size:.95rem;"></i></div>
                    <div>
                        <h5 class="font-weight-bold mb-0 text-title" style="font-size:1.05rem;">Security Features</h5>
                        <small class="text-muted">Account protection and access controls</small>
                    </div>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="d-flex align-items-center mb-1" style="gap:8px;">
                            <span class="font-weight-bold text-title" style="font-size:.92rem;">Two-Factor Authentication (2FA)</span>
                            <span class="sec-badge sec-orange" id="badge2FA"><i class="fas fa-exclamation-triangle" style="font-size:.65rem;"></i> Disabled</span>
                        </div>
                        <small class="text-muted">Enable OTP-based 2FA for secure portal logins</small>
                    </div>
                    <label class="toggle-switch mb-0">
                        <input type="checkbox" id="toggle2FA">
                        <span class="toggle-slider"></span>
                    </label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="d-flex align-items-center mb-1" style="gap:8px;">
                            <span class="font-weight-bold text-title" style="font-size:.92rem;">Login Session Alerts</span>
                            <span class="sec-badge sec-green"><i class="fas fa-check-circle" style="font-size:.65rem;"></i> Active</span>
                        </div>
                        <small class="text-muted">Get notified on new device logins</small>
                    </div>
                    <label class="toggle-switch mb-0">
                        <input type="checkbox" checked>
                        <span class="toggle-slider"></span>
                    </label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.92rem;">Password &amp; Access</div>
                        <small class="text-muted">Last changed: <span style="color:#10b981;font-weight:600;">Never</span></small>
                    </div>
                    <button type="button" class="btn btn-sm font-weight-bold px-3 py-1 rounded-pill" style="background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.3);color:#6366f1;font-size:.82rem;">
                        <i class="fas fa-key mr-1"></i>Change Password
                    </button>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="d-flex align-items-center mb-1" style="gap:8px;">
                            <span class="font-weight-bold text-title" style="font-size:.92rem;">IP Whitelist Protection</span>
                            <span class="sec-badge sec-orange" id="badgeIP"><i class="fas fa-minus-circle" style="font-size:.65rem;"></i> Off</span>
                        </div>
                        <small class="text-muted">Restrict console access to specific IP addresses</small>
                    </div>
                    <label class="toggle-switch mb-0">
                        <input type="checkbox" id="toggleIP">
                        <span class="toggle-slider"></span>
                    </label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="d-flex align-items-center mb-1" style="gap:8px;">
                            <span class="font-weight-bold text-title" style="font-size:.92rem;">Auto Session Timeout</span>
                            <span class="sec-badge sec-green"><i class="fas fa-check-circle" style="font-size:.65rem;"></i> 30 min</span>
                        </div>
                        <small class="text-muted">Automatically logout after inactivity</small>
                    </div>
                    <label class="toggle-switch mb-0">
                        <input type="checkbox" checked>
                        <span class="toggle-slider"></span>
                    </label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.92rem;">Active Login Sessions</div>
                        <small class="text-muted">Manage active sessions across devices</small>
                    </div>
                    <button type="button" class="btn btn-sm font-weight-bold px-3 py-1 rounded-pill" style="background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.3);color:#dc2626;font-size:.82rem;">
                        <i class="fas fa-sign-out-alt mr-1"></i>Revoke All
                    </button>
                </div>
            </div>

        </div>

        <!-- RIGHT: Real-Time Scenarios + Notifications -->
        <div class="col-lg-6 mb-4">

            <!-- Real-Time Fleet Scenarios Card -->
            <div class="settings-card mb-4" style="border-top-color:#f59e0b;">
                <div class="d-flex align-items-center mb-4">
                    <div class="section-icon" style="background:rgba(245,158,11,.12);"><i class="fas fa-satellite-dish" style="color:#f59e0b;font-size:.95rem;"></i></div>
                    <div class="flex-grow-1">
                        <h5 class="font-weight-bold mb-0 text-title" style="font-size:1.05rem;">Real-Time Fleet Scenarios</h5>
                        <small class="text-muted">Configure live fleet monitoring and auto-actions</small>
                    </div>
                    <span class="badge" style="background:rgba(245,158,11,.15);color:#d97706;font-size:.7rem;padding:4px 10px;border-radius:8px;font-weight:700;border:1px solid rgba(245,158,11,.3);white-space:nowrap;">
                        <span class="live-dot mr-1" style="background:#f59e0b;"></span>LIVE
                    </span>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.91rem;"><i class="fas fa-robot mr-2" style="color:#f59e0b;"></i>Auto-Complete Overdue Bookings</div>
                        <small class="text-muted">Auto mark bookings as Completed past drop date</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.91rem;"><i class="fas fa-bell mr-2" style="color:#f59e0b;"></i>New Booking Alert (Real-Time)</div>
                        <small class="text-muted">Live notification when a new booking arrives</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.91rem;"><i class="fas fa-tachometer-alt mr-2" style="color:#f59e0b;"></i>Fleet Telemetry Panel</div>
                        <small class="text-muted">Live fleet availability display on portal home</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.91rem;"><i class="fas fa-calendar-check mr-2" style="color:#f59e0b;"></i>Booking Conflict Detection</div>
                        <small class="text-muted">Flag double-bookings for the same vehicle/date</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.91rem;"><i class="fas fa-envelope-open-text mr-2" style="color:#f59e0b;"></i>Auto Confirmation Emails</div>
                        <small class="text-muted">Send confirmation email on booking approval</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox"><span class="toggle-slider"></span></label>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.91rem;"><i class="fas fa-chart-line mr-2" style="color:#f59e0b;"></i>Live Revenue Tracking</div>
                        <small class="text-muted">Show real-time revenue counters across portal</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>

                <div class="mt-3">
                    <button type="button" class="btn text-white font-weight-bold px-4 py-2 rounded-pill save-btn" style="background:linear-gradient(135deg,#f59e0b,#d97706);border:none;font-size:.88rem;">
                        <i class="fas fa-save mr-2"></i>Save Scenario Settings
                    </button>
                </div>
            </div>

            <!-- Notification Preferences Card -->
            <div class="settings-card" style="border-top-color:#10b981;">
                <div class="d-flex align-items-center mb-4">
                    <div class="section-icon"><i class="fas fa-bell" style="color:#10b981;font-size:.95rem;"></i></div>
                    <div>
                        <h5 class="font-weight-bold mb-0 text-title" style="font-size:1.05rem;">Notification Preferences</h5>
                        <small class="text-muted">Control what alerts and updates you receive</small>
                    </div>
                </div>

                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.9rem;">New Booking Submissions</div>
                        <small class="text-muted">Notify when a customer submits a rental request</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>
                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.9rem;">Booking Cancellations</div>
                        <small class="text-muted">Alert when a booking is cancelled by user</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>
                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.9rem;">Daily Fleet Summary Digest</div>
                        <small class="text-muted">Morning digest of bookings and revenue stats</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox"><span class="toggle-slider"></span></label>
                </div>
                <div class="setting-row">
                    <div>
                        <div class="font-weight-bold text-title mb-1" style="font-size:.9rem;">Fleet Utilisation Alerts</div>
                        <small class="text-muted">Alert when fleet utilisation exceeds 80%</small>
                    </div>
                    <label class="toggle-switch mb-0"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                </div>

                <div class="mt-3">
                    <button type="button" class="btn text-white font-weight-bold px-4 py-2 rounded-pill save-btn" style="background:linear-gradient(135deg,#10b981,#047857);border:none;font-size:.88rem;">
                        <i class="fas fa-check mr-2"></i>Save Notification Preferences
                    </button>
                </div>
            </div>

        </div>
    </div>

    <!-- Danger Zone -->
    <div class="settings-card mb-4" style="border-top-color:#ef4444;">
        <div class="d-flex align-items-center mb-3">
            <div class="section-icon" style="background:rgba(239,68,68,.1);"><i class="fas fa-exclamation-triangle" style="color:#ef4444;font-size:.95rem;"></i></div>
            <div>
                <h5 class="font-weight-bold mb-0" style="font-size:1.05rem;color:#dc2626;">Danger Zone</h5>
                <small class="text-muted">Irreversible administrative actions</small>
            </div>
        </div>
        <div class="d-flex flex-wrap align-items-center justify-content-between" style="gap:16px;">
            <div>
                <div class="font-weight-bold text-title mb-1" style="font-size:.9rem;">Reset All Dashboard Settings</div>
                <small class="text-muted">Restore all portal settings to factory defaults</small>
            </div>
            <button type="button" class="btn font-weight-bold px-4 py-2 rounded-pill" style="background:rgba(239,68,68,.1);border:1.5px solid rgba(239,68,68,.4);color:#dc2626;font-size:.88rem;">
                <i class="fas fa-undo mr-2"></i>Reset to Defaults
            </button>
        </div>
    </div>

</div>

<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
<script>
    // 2FA toggle badge
    document.getElementById('toggle2FA').addEventListener('change', function() {
        var b = document.getElementById('badge2FA');
        if (this.checked) {
            b.className = 'sec-badge sec-green';
            b.innerHTML = '<i class="fas fa-check-circle" style="font-size:.65rem;"></i> Enabled';
        } else {
            b.className = 'sec-badge sec-orange';
            b.innerHTML = '<i class="fas fa-exclamation-triangle" style="font-size:.65rem;"></i> Disabled';
        }
    });
    // IP whitelist badge
    document.getElementById('toggleIP').addEventListener('change', function() {
        var b = document.getElementById('badgeIP');
        if (this.checked) {
            b.className = 'sec-badge sec-green';
            b.innerHTML = '<i class="fas fa-check-circle" style="font-size:.65rem;"></i> Protected';
        } else {
            b.className = 'sec-badge sec-orange';
            b.innerHTML = '<i class="fas fa-minus-circle" style="font-size:.65rem;"></i> Off';
        }
    });
    // Save button flash
    document.querySelectorAll('.save-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var orig = this.innerHTML;
            var origBg = this.style.background;
            this.innerHTML = '<i class="fas fa-check mr-2"></i>Saved!';
            this.style.background = 'linear-gradient(135deg,#059669,#047857)';
            var self = this;
            setTimeout(function() { self.innerHTML = orig; self.style.background = origBg; }, 2000);
        });
    });
</script>
</body>
</html>"""

out_path = r'templates/portal_rental_profile.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Written:', len(html), 'chars')
