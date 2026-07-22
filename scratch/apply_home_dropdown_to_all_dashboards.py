import os

base_dir = r"c:\Users\DELL\python\Ride Share\demo\demo\myproject"
templates_dir = os.path.join(base_dir, "templates")

# Shared CSS helper block
shared_dropdown_css = """
        /* Dynamic Premium Dropdown Menu Card - Dashboard Matching Colors */
        .premium-user-dropdown {
            min-width: 295px !important;
            border-radius: 16px !important;
            overflow: hidden !important;
            padding: 0 !important;
            margin-top: 8px !important;
            animation: dropdownSlideIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
            transform-origin: top left !important;
        }

        @keyframes dropdownSlideIn {
            from { opacity: 0; transform: scale(0.95) translateY(-8px); }
            to { opacity: 1; transform: scale(1) translateY(0); }
        }

        .dropdown-section-label {
            font-size: 0.6rem !important;
            font-weight: 800 !important;
            letter-spacing: 0.8px !important;
            text-transform: uppercase !important;
            padding: 4px 14px 2px 14px !important;
            margin: 0 !important;
        }

        .premium-dropdown-item {
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            padding: 5px 10px !important;
            text-decoration: none !important;
            transition: all 0.2s ease !important;
            background: transparent !important;
            border: none !important;
            border-radius: 8px !important;
            margin: 1px 6px !important;
            width: calc(100% - 12px) !important;
        }

        .premium-dropdown-item:hover {
            transform: translateX(3px) !important;
            text-decoration: none !important;
        }

        .dropdown-icon-box {
            width: 28px !important;
            height: 28px !important;
            border-radius: 8px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 0.8rem !important;
            margin-right: 8px !important;
            transition: all 0.2s ease !important;
        }

        /* Profile & Settings and Logout Colored Items */
        .item-colored-theme-emerald { background: rgba(16, 185, 129, 0.14) !important; }
        .item-colored-theme-emerald .dropdown-item-title { color: #059669 !important; font-weight: 750 !important; }

        .item-colored-theme-amber { background: rgba(245, 158, 11, 0.14) !important; }
        .item-colored-theme-amber .dropdown-item-title { color: #d97706 !important; font-weight: 750 !important; }

        .item-colored-theme-purple { background: rgba(236, 72, 153, 0.14) !important; }
        .item-colored-theme-purple .dropdown-item-title { color: #be185d !important; font-weight: 750 !important; }

        .item-colored-logout { background: rgba(239, 68, 68, 0.14) !important; }
        .item-colored-logout .dropdown-item-title { color: #dc2626 !important; font-weight: 750 !important; }

        /* Remaining pages dark black text color */
        .dropdown-item-title {
            font-size: 0.8rem !important;
            font-weight: 750 !important;
            color: #0f172a !important; /* Crisp Dark Black text color */
            margin-bottom: 0 !important;
            line-height: 1.15 !important;
        }

        .dropdown-item-sub {
            font-size: 0.65rem !important;
            color: #64748b !important;
            font-weight: 500 !important;
        }

        .dropdown-divider-premium {
            height: 1px !important;
            margin: 3px 10px !important;
            background: rgba(226, 232, 240, 0.8) !important;
        }
"""

# Rental Dropdown Markup
rental_dropdown_markup = """<div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 295px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 16px; border: 1.5px solid rgba(16, 185, 129, 0.4); box-shadow: 0 16px 45px rgba(16, 185, 129, 0.18), 0 4px 15px rgba(0,0,0,0.08); background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px);">
                    <!-- Dynamic Compact Menu Header -->
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%) !important; padding: 10px 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.18) !important;">
                        <div class="d-flex align-items-center">
                            <div style="width: 32px; height: 32px; border-radius: 10px; background: rgba(255,255,255,0.22); display: flex; align-items: center; justify-content: center; margin-right: 10px; backdrop-filter: blur(4px);">
                                <i class="fas fa-car-side" style="font-size: 14px; color: #ffffff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-white" style="font-size: 0.82rem; line-height: 1.1;">Rental Settings Console</h6>
                                <small class="text-white-50" style="font-size: 0.65rem;"><i class="fas fa-circle text-light mr-1" style="font-size: 5px;"></i>Live Telemetry</small>
                            </div>
                        </div>
                        <span class="badge" style="background: rgba(255,255,255,0.25); color: #ffffff; font-size: 0.6rem; padding: 3px 6px; border-radius: 8px; font-weight: 700;">Rental Manager</span>
                    </div>

                    <div class="py-1">
                        <div class="dropdown-section-label" style="color: #059669 !important;">Profile &amp; Account</div>
                        <a class="premium-dropdown-item item-colored-theme-emerald" href="{% url 'portal_rental_profile' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(16, 185, 129, 0.2); color: #059669;">
                                    <i class="fas fa-user-cog"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Profile &amp; Settings</div>
                                    <div class="dropdown-item-sub">Fleet Admin Profile &amp; Image</div>
                                </div>
                            </div>
                            <span class="badge" style="background: rgba(16, 185, 129, 0.15); color: #059669; font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; font-weight: 700;"><i class="fas fa-shield-alt mr-1"></i>Verified</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <div class="dropdown-section-label" style="color: #059669 !important;">Fleet Controls</div>
                        <a class="premium-dropdown-item" href="#" data-toggle="modal" data-target="#addNewVehicleModal">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(2, 132, 199, 0.14); color: #0284c7;">
                                    <i class="fas fa-car"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Add New Vehicle</div>
                                    <div class="dropdown-item-sub">Register Showroom Car</div>
                                </div>
                            </div>
                            <span class="badge" style="background: rgba(2, 132, 199, 0.12); color: #0284c7; font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; font-weight: 700;"><i class="fas fa-plus mr-1"></i>Add Fleet</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rental_bookings' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(99, 102, 241, 0.14); color: #6366f1;">
                                    <i class="fas fa-book"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Booking Requests</div>
                                    <div class="dropdown-item-sub">Manage Confirmations</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(99, 102, 241, 0.15); color: #4f46e5; font-weight: 700;"><i class="fas fa-sync-alt fa-spin mr-1" style="font-size: 7px;"></i>Live Log</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rental_remaining' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(245, 158, 11, 0.14); color: #f59e0b;">
                                    <i class="fas fa-clipboard-list"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Remaining Fleet</div>
                                    <div class="dropdown-item-sub">Active Inventory</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(245, 158, 11, 0.15); color: #b45309; font-weight: 700;">Active</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rental_completed' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(16, 185, 129, 0.14); color: #10b981;">
                                    <i class="fas fa-check-double"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Rides Completed</div>
                                    <div class="dropdown-item-sub">Finished Rentals</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(16, 185, 129, 0.15); color: #059669; font-weight: 700;">Done</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="/">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(139, 92, 246, 0.14); color: #8b5cf6;">
                                    <i class="fas fa-exchange-alt"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Exit to User Portal</div>
                                    <div class="dropdown-item-sub">Return to Home</div>
                                </div>
                            </div>
                            <i class="fas fa-chevron-right text-muted" style="font-size: 0.6rem; opacity: 0.4;"></i>
                        </a>
                        <a class="premium-dropdown-item item-colored-logout" href="{% url 'portal_logout' %}">
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
                </div>"""

# Rider Dropdown Markup with Profile & Settings
rider_dropdown_markup = """<div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 295px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 16px; border: 1.5px solid rgba(245, 158, 11, 0.4); box-shadow: 0 16px 45px rgba(245, 158, 11, 0.18), 0 4px 15px rgba(0,0,0,0.08); background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px);">
                    <!-- Dynamic Compact Menu Header -->
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%) !important; padding: 10px 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.18) !important;">
                        <div class="d-flex align-items-center">
                            <div style="width: 32px; height: 32px; border-radius: 10px; background: rgba(255,255,255,0.22); display: flex; align-items: center; justify-content: center; margin-right: 10px; backdrop-filter: blur(4px);">
                                <i class="fas fa-motorcycle" style="font-size: 14px; color: #ffffff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-white" style="font-size: 0.82rem; line-height: 1.1;">Chauffeur Console</h6>
                                <small class="text-white-50" style="font-size: 0.65rem;"><i class="fas fa-circle text-light mr-1" style="font-size: 5px;"></i>Live Dispatch</small>
                            </div>
                        </div>
                        <span class="badge" style="background: rgba(255,255,255,0.25); color: #ffffff; font-size: 0.6rem; padding: 3px 6px; border-radius: 8px; font-weight: 700;">Active Rider</span>
                    </div>

                    <div class="py-1">
                        <div class="dropdown-section-label" style="color: #d97706 !important;">Rider Profile &amp; Controls</div>
                        <a class="premium-dropdown-item item-colored-theme-amber" href="{% url 'portal_rider_profile' %}">
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

                        <a class="premium-dropdown-item" href="{% url 'portal_rider_active' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(2, 132, 199, 0.14); color: #0284c7;">
                                    <i class="fas fa-motorcycle"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Active Rides</div>
                                    <div class="dropdown-item-sub">Live Trip Dashboard</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(2, 132, 199, 0.15); color: #0284c7; font-weight: 700;"><i class="fas fa-satellite-dish mr-1"></i>On Duty</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rider_trips' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(99, 102, 241, 0.14); color: #6366f1;">
                                    <i class="fas fa-history"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Ride History</div>
                                    <div class="dropdown-item-sub">Completed Trips Log</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(99, 102, 241, 0.12); color: #4f46e5; font-weight: 700;">Logs</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_rider_earnings' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(16, 185, 129, 0.14); color: #10b981;">
                                    <i class="fas fa-wallet"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Total Earnings</div>
                                    <div class="dropdown-item-sub">Payouts &amp; Analytics</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(16, 185, 129, 0.15); color: #059669; font-weight: 700;">Payouts</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="/">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(139, 92, 246, 0.14); color: #8b5cf6;">
                                    <i class="fas fa-exchange-alt"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Exit to User Portal</div>
                                    <div class="dropdown-item-sub">Return to Home</div>
                                </div>
                            </div>
                            <i class="fas fa-chevron-right text-muted" style="font-size: 0.6rem; opacity: 0.4;"></i>
                        </a>
                        <a class="premium-dropdown-item item-colored-logout" href="{% url 'portal_logout' %}">
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
                </div>"""

# Carpool Dropdown Markup with Profile & Settings
carpool_dropdown_markup = """<div class="dropdown-menu premium-user-dropdown" aria-labelledby="dashboardDropdown" style="position: absolute !important; left: 0 !important; right: auto !important; margin-top: 8px !important; transform-origin: top left !important; min-width: 295px !important; z-index: 1050 !important; padding: 0; overflow: hidden; border-radius: 16px; border: 1.5px solid rgba(236, 72, 153, 0.4); box-shadow: 0 16px 45px rgba(236, 72, 153, 0.18), 0 4px 15px rgba(0,0,0,0.08); background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; backdrop-filter: blur(20px);">
                    <!-- Dynamic Compact Menu Header -->
                    <div class="dropdown-user-header d-flex align-items-center justify-content-between" style="background: linear-gradient(135deg, #ec4899 0%, #d946ef 50%, #a855f7 100%) !important; padding: 10px 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.18) !important;">
                        <div class="d-flex align-items-center">
                            <div style="width: 32px; height: 32px; border-radius: 10px; background: rgba(255,255,255,0.22); display: flex; align-items: center; justify-content: center; margin-right: 10px; backdrop-filter: blur(4px);">
                                <i class="fas fa-users" style="font-size: 14px; color: #ffffff;"></i>
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-white" style="font-size: 0.82rem; line-height: 1.1;">Pooling Console</h6>
                                <small class="text-white-50" style="font-size: 0.65rem;"><i class="fas fa-circle text-light mr-1" style="font-size: 5px;"></i>Shared Network</small>
                            </div>
                        </div>
                        <span class="badge" style="background: rgba(255,255,255,0.25); color: #ffffff; font-size: 0.6rem; padding: 3px 6px; border-radius: 8px; font-weight: 700;">Pool Host</span>
                    </div>

                    <div class="py-1">
                        <div class="dropdown-section-label" style="color: #be185d !important;">Pooling Profile &amp; Controls</div>
                        <a class="premium-dropdown-item item-colored-theme-purple" href="{% url 'portal_carpool_profile' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(236, 72, 153, 0.2); color: #be185d;">
                                    <i class="fas fa-user-cog"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Profile &amp; Settings</div>
                                    <div class="dropdown-item-sub">Host Profile &amp; Image</div>
                                </div>
                            </div>
                            <span class="badge" style="background: rgba(236, 72, 153, 0.15); color: #be185d; font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; font-weight: 700;"><i class="fas fa-shield-alt mr-1"></i>Verified Host</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="{% url 'portal_carpool_publish' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(244, 63, 94, 0.14); color: #f43f5e;">
                                    <i class="fas fa-plus-circle"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Publish New Ride</div>
                                    <div class="dropdown-item-sub">Create Shared Route</div>
                                </div>
                            </div>
                            <span class="badge" style="background: rgba(244, 63, 94, 0.12); color: #e11d48; font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; font-weight: 700;"><i class="fas fa-plus mr-1"></i>New Route</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_carpool_itineraries' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(2, 132, 199, 0.14); color: #0284c7;">
                                    <i class="fas fa-route"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Pooled Itineraries</div>
                                    <div class="dropdown-item-sub">Scheduled Rides</div>
                                </div>
                            </div>
                            <span class="badge" style="font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; background: rgba(2, 132, 199, 0.15); color: #0284c7; font-weight: 700;"><i class="fas fa-sync-alt fa-spin mr-1" style="font-size: 7px;"></i>Live</span>
                        </a>
                        <a class="premium-dropdown-item" href="{% url 'portal_carpool_bookings' %}">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(99, 102, 241, 0.14); color: #6366f1;">
                                    <i class="fas fa-users"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Booking Requests</div>
                                    <div class="dropdown-item-sub">Passenger Seat Claims</div>
                                </div>
                            </div>
                            <span class="badge" style="background: rgba(99, 102, 241, 0.12); color: #4f46e5; font-size: 0.58rem; padding: 2px 5px; border-radius: 5px; font-weight: 700;">Claims</span>
                        </a>

                        <div class="dropdown-divider-premium"></div>

                        <a class="premium-dropdown-item" href="/">
                            <div class="d-flex align-items-center">
                                <div class="dropdown-icon-box" style="background: rgba(245, 158, 11, 0.14); color: #f59e0b;">
                                    <i class="fas fa-exchange-alt"></i>
                                </div>
                                <div>
                                    <div class="dropdown-item-title">Exit to User Portal</div>
                                    <div class="dropdown-item-sub">Return to Home</div>
                                </div>
                            </div>
                            <i class="fas fa-chevron-right text-muted" style="font-size: 0.6rem; opacity: 0.4;"></i>
                        </a>
                        <a class="premium-dropdown-item item-colored-logout" href="{% url 'portal_logout' %}">
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
                </div>"""

def process_file(filepath, markup_type):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if markup_type == 'rental':
        markup = rental_dropdown_markup
    elif markup_type == 'rider':
        markup = rider_dropdown_markup
    elif markup_type == 'carpool':
        markup = carpool_dropdown_markup

    trigger_pos = content.find('id="dashboardDropdown"')
    if trigger_pos != -1:
        menu_start = content.find('<div class="dropdown-menu', trigger_pos)
        if menu_start != -1:
            depth = 0
            menu_end = -1
            i = menu_start
            while i < len(content):
                if content[i:i+4] == '<div':
                    depth += 1
                elif content[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        menu_end = i + 6
                        break
                i += 1

            if menu_end != -1:
                content = content[:menu_start] + markup + content[menu_end:]

    if '.item-colored-theme-emerald' not in content:
        style_idx = content.find('</style>')
        if style_idx != -1:
            content = content[:style_idx] + shared_dropdown_css + "\n" + content[style_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for fname in os.listdir(templates_dir):
    if fname.startswith('portal_rental'):
        process_file(os.path.join(templates_dir, fname), 'rental')
    elif fname.startswith('portal_rider'):
        process_file(os.path.join(templates_dir, fname), 'rider')
    elif fname.startswith('portal_carpool'):
        process_file(os.path.join(templates_dir, fname), 'carpool')

print("Applied Profile & Settings link, theme colored Profile & Logout items, and dark black text titles across all partner portal dropdowns!")
