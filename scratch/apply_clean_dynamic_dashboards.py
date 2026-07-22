import os, re

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

# 1. Rider Console Dropdown HTML
rider_dropdown = """<div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 250px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 14px; border: 1px solid rgba(245, 158, 11, 0.3); box-shadow: 0 14px 40px rgba(0,0,0,0.18); background-color: var(--card-bg, #ffffff) !important; backdrop-filter: blur(10px);">
                    <!-- Dynamic Menu Header -->
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%) !important; padding: 12px 16px;">
                        <div class="d-flex align-items-center">
                            <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                                <i class="fas fa-motorcycle" style="font-size: 18px; color: #ffffff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold" style="color: #ffffff; font-size: 0.88rem; letter-spacing: 0.3px;">Chauffeur Console</h6>
                                <small class="text-white-50" style="font-size: 0.68rem;"><i class="fas fa-circle text-success mr-1" style="font-size: 6px;"></i>Live Controls &amp; Options</small>
                            </div>
                        </div>
                    </div>

                    <style>
                        .dropdown-item-amber {
                            color: #f59e0b !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-weight: 600;
                            font-size: 0.83rem;
                        }
                        .dropdown-item-amber:hover {
                            background-color: rgba(245, 158, 11, 0.12) !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                        .dropdown-item-red {
                            color: #ef4444 !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-weight: 600;
                            font-size: 0.83rem;
                        }
                        .dropdown-item-red:hover {
                            background-color: rgba(239, 68, 68, 0.12) !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                        .dropdown-item-normal {
                            color: var(--text-color, #1e293b) !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-size: 0.83rem;
                            font-weight: 500;
                        }
                        .dropdown-item-normal:hover {
                            background-color: rgba(245, 158, 11, 0.08) !important;
                            color: #d97706 !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                    </style>

                    <div class="py-1" style="background-color: var(--card-bg, #ffffff) !important;">
                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <a class="dropdown-item-amber" href="{% url 'portal_rider' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-user-cog" style="width: 16px;"></i><span>Profile &amp; Settings</span>
                                    </div>
                                    <i class="fas fa-chevron-right" style="font-size: 0.65rem; opacity: 0.6;"></i>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>
                        <div class="px-3 py-1 font-weight-bold text-uppercase text-muted" style="font-size: 0.62rem; letter-spacing: 0.6px; color: #f59e0b !important;">Real-Time Controls</div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-robot text-warning mr-1" style="width: 16px;"></i><span>Auto-Accept</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-rider-autoaccept" checked onclick="showToast('Auto-Accept Status Updated')">
                                        <label class="custom-control-label" for="switch-rider-autoaccept"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-fire text-warning mr-1" style="width: 16px;"></i><span>Demand Heatmap</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-rider-heatmap" checked onclick="showToast('Live Demand Heatmap Layer Toggled')">
                                        <label class="custom-control-label" for="switch-rider-heatmap"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="#" onclick="showToast('Surge Area Boost: 1.5x active')">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-chart-line text-warning mr-1" style="width: 16px;"></i><span>Surge Boost</span>
                                    </div>
                                    <span class="badge" style="font-size: 0.65rem; padding: 3px 8px; border-radius: 10px; background: linear-gradient(135deg, #f59e0b, #d97706); color: #fff; font-weight: 700;">1.5x</span>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>
                        <div class="px-3 py-1 font-weight-bold text-uppercase text-muted" style="font-size: 0.62rem; letter-spacing: 0.6px; color: #94a3b8 !important;">Console Settings</div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <a class="dropdown-item-normal" href="#" onclick="showToast('Routing to nearest Gas Station...')">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-gas-pump text-muted mr-1" style="width: 16px;"></i><span>Gas Nav</span>
                                    </div>
                                    <i class="fas fa-location-arrow text-muted" style="font-size: 0.65rem;"></i>
                                </a>
                            </li>
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-volume-up text-muted mr-1" style="width: 16px;"></i><span>Audio Alerts</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-rider-sound" checked onclick="showToast('Console Sounds Muted/Unmuted')">
                                        <label class="custom-control-label" for="switch-rider-sound"></label>
                                    </div>
                                </div>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 4px;">
                            <li>
                                <a class="dropdown-item-normal" href="{% url 'home' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-home text-muted mr-1" style="width: 16px;"></i><span>Exit to User Portal</span>
                                    </div>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item-red" href="{% url 'portal_logout' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-sign-out-alt mr-1" style="width: 16px;"></i><span>Logout</span>
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>"""

# 2. Rental Console Dropdown HTML
rental_dropdown = """<div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 250px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 14px; border: 1px solid rgba(16, 185, 129, 0.3); box-shadow: 0 14px 40px rgba(0,0,0,0.18); background-color: var(--card-bg, #ffffff) !important; backdrop-filter: blur(10px);">
                    <!-- Dynamic Menu Header -->
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #10b981 0%, #047857 100%) !important; padding: 12px 16px;">
                        <div class="d-flex align-items-center">
                            <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                                <i class="fas fa-car-side" style="font-size: 18px; color: #ffffff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold" style="color: #ffffff; font-size: 0.88rem; letter-spacing: 0.3px;">Rental Settings Console</h6>
                                <small class="text-white-50" style="font-size: 0.68rem;"><i class="fas fa-circle text-light mr-1" style="font-size: 6px;"></i>Fleet Active Controls</small>
                            </div>
                        </div>
                    </div>

                    <style>
                        .dropdown-item-green {
                            color: #10b981 !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-weight: 600;
                            font-size: 0.83rem;
                        }
                        .dropdown-item-green:hover {
                            background-color: rgba(16, 185, 129, 0.12) !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                        .dropdown-item-red {
                            color: #ef4444 !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-weight: 600;
                            font-size: 0.83rem;
                        }
                        .dropdown-item-red:hover {
                            background-color: rgba(239, 68, 68, 0.12) !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                        .dropdown-item-normal {
                            color: var(--text-color, #1e293b) !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-size: 0.83rem;
                            font-weight: 500;
                        }
                        .dropdown-item-normal:hover {
                            background-color: rgba(16, 185, 129, 0.08) !important;
                            color: #059669 !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                    </style>

                    <div class="py-1" style="background-color: var(--card-bg, #ffffff) !important;">
                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <a class="dropdown-item-green" href="{% url 'portal_rental' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-user-cog" style="width: 16px;"></i><span>Profile &amp; Settings</span>
                                    </div>
                                    <i class="fas fa-chevron-right" style="font-size: 0.65rem; opacity: 0.6;"></i>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>
                        <div class="px-3 py-1 font-weight-bold text-uppercase text-muted" style="font-size: 0.62rem; letter-spacing: 0.6px; color: #10b981 !important;">Real-Time Controls</div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-tools text-success mr-1" style="width: 16px;"></i><span>Maintenance Mode</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-rental-maintenance" onclick="showToast('Fleet Auto-deactivation settings updated')">
                                        <label class="custom-control-label" for="switch-rental-maintenance"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-map-marker-alt text-success mr-1" style="width: 16px;"></i><span>Live GPS Tracking</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-rental-gps" checked onclick="showToast('Live Fleet Tracking active')">
                                        <label class="custom-control-label" for="switch-rental-gps"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="{% url 'portal_rental_bookings' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-bell text-success mr-1" style="width: 16px;"></i><span>Booking Alerts</span>
                                    </div>
                                    <span class="badge" style="font-size: 0.65rem; padding: 3px 8px; border-radius: 10px; background: linear-gradient(135deg, #10b981, #059669); color: #fff; font-weight: 700;">3 Active</span>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="{% url 'portal_rental_completed' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-check-circle text-success mr-1" style="width: 16px;"></i><span>Completed Rides</span>
                                    </div>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>
                        <div class="px-3 py-1 font-weight-bold text-uppercase text-muted" style="font-size: 0.62rem; letter-spacing: 0.6px; color: #94a3b8 !important;">Console Settings</div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <a class="dropdown-item-normal" href="#" onclick="showToast('Security deposit configuration set')">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-shield-alt text-muted mr-1" style="width: 16px;"></i><span>Deposit Level</span>
                                    </div>
                                    <span class="badge badge-secondary" style="font-size: 0.65rem; padding: 3px 8px; border-radius: 10px;">₹5,000</span>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="#" onclick="showToast('Gold Partner payout benefits active')">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-star text-warning mr-1" style="width: 16px;"></i><span>Partner Tier</span>
                                    </div>
                                    <span class="badge" style="font-size: 0.65rem; padding: 3px 8px; border-radius: 10px; background: #f59e0b; color: #fff; font-weight: 700;">Gold</span>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 4px;">
                            <li>
                                <a class="dropdown-item-normal" href="{% url 'home' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-home text-muted mr-1" style="width: 16px;"></i><span>Exit to User Portal</span>
                                    </div>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item-red" href="{% url 'portal_logout' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-sign-out-alt mr-1" style="width: 16px;"></i><span>Logout</span>
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>"""

# 3. Pooling Console Dropdown HTML
carpool_dropdown = """<div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 250px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 14px; border: 1px solid rgba(236, 72, 153, 0.3); box-shadow: 0 14px 40px rgba(0,0,0,0.18); background-color: var(--card-bg, #ffffff) !important; backdrop-filter: blur(10px);">
                    <!-- Dynamic Menu Header -->
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #ec4899 0%, #be185d 100%) !important; padding: 12px 16px;">
                        <div class="d-flex align-items-center">
                            <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                                <i class="fas fa-users" style="font-size: 18px; color: #ffffff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold" style="color: #ffffff; font-size: 0.88rem; letter-spacing: 0.3px;">Pooling Settings Console</h6>
                                <small class="text-white-50" style="font-size: 0.68rem;"><i class="fas fa-circle text-light mr-1" style="font-size: 6px;"></i>Commuter Network Live</small>
                            </div>
                        </div>
                    </div>

                    <style>
                        .dropdown-item-pink {
                            color: #ec4899 !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-weight: 600;
                            font-size: 0.83rem;
                        }
                        .dropdown-item-pink:hover {
                            background-color: rgba(236, 72, 153, 0.12) !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                        .dropdown-item-red {
                            color: #ef4444 !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-weight: 600;
                            font-size: 0.83rem;
                        }
                        .dropdown-item-red:hover {
                            background-color: rgba(239, 68, 68, 0.12) !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                        .dropdown-item-normal {
                            color: var(--text-color, #1e293b) !important;
                            background-color: transparent !important;
                            border-radius: 8px;
                            padding: 6px 12px;
                            margin: 3px 6px;
                            display: flex;
                            align-items: center;
                            justify-content: space-between;
                            text-decoration: none;
                            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
                            font-size: 0.83rem;
                            font-weight: 500;
                        }
                        .dropdown-item-normal:hover {
                            background-color: rgba(236, 72, 153, 0.08) !important;
                            color: #db2777 !important;
                            transform: translateX(3px);
                            text-decoration: none !important;
                        }
                    </style>

                    <div class="py-1" style="background-color: var(--card-bg, #ffffff) !important;">
                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <a class="dropdown-item-pink" href="{% url 'portal_carpool' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-user-cog" style="width: 16px;"></i><span>Profile &amp; Settings</span>
                                    </div>
                                    <i class="fas fa-chevron-right" style="font-size: 0.65rem; opacity: 0.6;"></i>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>
                        <div class="px-3 py-1 font-weight-bold text-uppercase text-muted" style="font-size: 0.62rem; letter-spacing: 0.6px; color: #ec4899 !important;">Real-Time Controls</div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-sync-alt text-danger mr-1" style="width: 16px; color: #ec4899 !important;"></i><span>Auto-Match</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-pool-automatch" checked onclick="showToast('Auto-Match Preferences updated')">
                                        <label class="custom-control-label" for="switch-pool-automatch"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="#" onclick="showToast('Calculating dynamic fuel share splits...')">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-calculator text-muted mr-1" style="width: 16px;"></i><span>Fuel Split Calc</span>
                                    </div>
                                    <i class="fas fa-calculator text-muted" style="font-size: 0.65rem;"></i>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="{% url 'portal_carpool_bookings' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-bell mr-1" style="width: 16px; color: #ec4899 !important;"></i><span>Match Alerts</span>
                                    </div>
                                    <span class="badge" style="font-size: 0.65rem; padding: 3px 8px; border-radius: 10px; background: linear-gradient(135deg, #ec4899, #be185d); color: #fff; font-weight: 700;">4 Pending</span>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>
                        <div class="px-3 py-1 font-weight-bold text-uppercase text-muted" style="font-size: 0.62rem; letter-spacing: 0.6px; color: #94a3b8 !important;">Console Settings</div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 2px;">
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-female text-muted mr-1" style="width: 16px;"></i><span>Girls-Only Pool</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-pool-womenonly" onclick="showToast('Girls-Only matching mode toggled')">
                                        <label class="custom-control-label" for="switch-pool-womenonly"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <div class="dropdown-item-normal">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-paw text-muted mr-1" style="width: 16px;"></i><span>Pets Allowed</span>
                                    </div>
                                    <div class="custom-control custom-switch">
                                        <input type="checkbox" class="custom-control-input" id="switch-pool-pets" onclick="showToast('Pet allowance preferences updated')">
                                        <label class="custom-control-label" for="switch-pool-pets"></label>
                                    </div>
                                </div>
                            </li>
                            <li>
                                <a class="dropdown-item-normal" href="#" onclick="showToast('Maximum luggage limit set')">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-suitcase text-muted mr-1" style="width: 16px;"></i><span>Max Luggage</span>
                                    </div>
                                    <span class="badge badge-secondary" style="font-size: 0.65rem; padding: 3px 8px; border-radius: 10px;">2 Bags</span>
                                </a>
                            </li>
                        </ul>

                        <div class="dropdown-divider-premium" style="height: 1px; background-color: rgba(0,0,0,0.06); margin: 4px 6px;"></div>

                        <ul class="dropdown-list-container" style="list-style: none; padding: 0; margin-bottom: 4px;">
                            <li>
                                <a class="dropdown-item-normal" href="{% url 'home' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-home text-muted mr-1" style="width: 16px;"></i><span>Exit to User Portal</span>
                                    </div>
                                </a>
                            </li>
                            <li>
                                <a class="dropdown-item-red" href="{% url 'portal_logout' %}">
                                    <div class="d-flex align-items-center" style="gap: 8px;">
                                        <i class="fas fa-sign-out-alt mr-1" style="width: 16px;"></i><span>Logout</span>
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>"""

rider_files = ["portal_rider.html", "portal_rider_active.html", "portal_rider_earnings.html", "portal_rider_trips.html"]
rental_files = ["portal_rental.html", "portal_rental_bookings.html", "portal_rental_cars.html", "portal_rental_completed.html", "portal_rental_remaining.html"]
carpool_files = ["portal_carpool.html", "portal_carpool_bookings.html", "portal_carpool_itineraries.html", "portal_carpool_publish.html"]

def clean_update_file(fname, dropdown_code, brand_url_name, brand_text, live_badge_html):
    fpath = os.path.join(templates_dir, fname)
    if not os.path.exists(fpath):
        return
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find start of dropdown menu
    start_tag = '<div class="dropdown-menu premium-user-dropdown"'
    end_tag = f'<a class="navbar-brand font-weight-bold" href="{{% url \'{brand_url_name}\' %}}"'
    
    # If standard brand link format:
    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag)
        end_idx = content.find(end_tag)
        
        new_middle = dropdown_code + "\n            </div>\n            \n            "
        new_brand = f'<a class="navbar-brand font-weight-bold d-flex align-items-center" href="{{% url \'{brand_url_name}\' %}}" style="margin-bottom: 0; align-self: center; font-size: 1.15rem; gap: 8px;">{brand_text}{live_badge_html}</a>'
        
        # find end of brand tag
        brand_close_idx = content.find("</a>", end_idx) + 4
        
        content = content[:start_idx] + new_middle + new_brand + content[brand_close_idx:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Clean updated {fname}")
    else:
        print(f"Tags not found in {fname}")

rider_badge = '<span class="badge badge-warning ml-2" style="font-size: 0.68rem; padding: 4px 9px; border-radius: 12px; background: rgba(245,158,11,0.25); color: #ffffff; border: 1px solid rgba(255,255,255,0.4);"><i class="fas fa-bolt text-warning mr-1"></i>Active</span>'
rental_badge = '<span class="badge badge-success ml-2" style="font-size: 0.68rem; padding: 4px 9px; border-radius: 12px; background: rgba(16,185,129,0.25); color: #ffffff; border: 1px solid rgba(255,255,255,0.4);"><i class="fas fa-check-circle text-light mr-1"></i>Fleet Live</span>'
carpool_badge = '<span class="badge ml-2" style="font-size: 0.68rem; padding: 4px 9px; border-radius: 12px; background: rgba(236,72,153,0.25); color: #ffffff; border: 1px solid rgba(255,255,255,0.4);"><i class="fas fa-wifi text-light mr-1"></i>Pool Online</span>'

for f in rider_files:
    clean_update_file(f, rider_dropdown, "portal_rider", '<i class="fas fa-motorcycle mr-2"></i>Chauffeur Console', rider_badge)

for f in rental_files:
    clean_update_file(f, rental_dropdown, "portal_rental", '<i class="fas fa-car mr-2"></i>Fleet Rental Console', rental_badge)

for f in carpool_files:
    clean_update_file(f, carpool_dropdown, "portal_carpool", '<i class="fas fa-users mr-2"></i>Commuter Pool Console', carpool_badge)

print("Clean update finished!")
