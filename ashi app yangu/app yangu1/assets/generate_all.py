import json
import os

# ============================================================
# CENTRAL ASSET DIRECTORIES
# ============================================================

base_dir = "assets"

worlds_dir = os.path.join(base_dir, "worlds")
shaders_dir = os.path.join(base_dir, "shaders")
locales_dir = os.path.join(base_dir, "locales")
config_dir = os.path.join(base_dir, "config")
presets_dir = os.path.join(base_dir, "presets")
docs_dir = "docs"

for directory in [
    worlds_dir,
    shaders_dir,
    locales_dir,
    config_dir,
    presets_dir,
    docs_dir
]:
    os.makedirs(directory, exist_ok=True)

# ============================================================
# 1. ADVANCED ENVIRONMENT SHADER
# ============================================================

advanced_shader_content = """#version 300 es
precision highp float;

in vec2 vTexCoord;
out vec4 fragColor;

uniform sampler2D uPanoramaTexture;

uniform float uYawAngle;
uniform float uPitchAngle;
uniform float uTime;

uniform vec3 uColorFilter;

uniform float uWindIntensity;
uniform float uBloomThreshold;
uniform float uFogDensity;

uniform float uRainIntensity;
uniform float uSnowIntensity;
uniform float uCloudSpeed;
uniform float uDayNight;
uniform float uEnvironmentBrightness;

void main() {

vec2 uv = vTexCoord;  

float windEffect =  
    sin(uv.y * 25.0 + uTime * 4.0)  
    * 0.004  
    * uWindIntensity;  

float windWave =  
    cos(uv.x * 15.0 + uTime * 2.5)  
    * 0.002  
    * uWindIntensity;  

uv.x += windEffect;  
uv.y += windWave;  

uv.x = fract(  
    uv.x + uYawAngle / 360.0  
);  

uv.y = clamp(  
    uv.y + uPitchAngle / 180.0,  
    0.0,  
    1.0  
);  

vec4 texColor =  
    texture(uPanoramaTexture, uv);  

vec3 color =  
    texColor.rgb * uColorFilter;  

float daylight =  
    mix(  
        0.25,  
        1.0,  
        uDayNight  
    );  

color *=  
    daylight *  
    uEnvironmentBrightness;  

float sunRay =  
    max(  
        0.0,  
        sin(  
            uv.x * 3.14159 * 4.0  
            + uTime * 0.5  
        )  
    );  

color +=  
    vec3(0.12, 0.10, 0.08)  
    * sunRay  
    * uWindIntensity;  

float brightness =  
    dot(  
        color,  
        vec3(  
            0.2126,  
            0.7152,  
            0.0722  
        )  
    );  

if (  
    brightness >  
    uBloomThreshold  
) {  
    color +=  
        color * 0.35;  
}  

float fogFactor =  
    smoothstep(  
        0.2,  
        0.9,  
        abs(  
            uv.y - 0.5  
        )  
    )  
    * uFogDensity;  

color =  
    mix(  
        color,  
        vec3(  
            0.05,  
            0.08,  
            0.12  
        ),  
        fogFactor  
    );  

float rain =  
    fract(  
        sin(  
            dot(  
                uv,  
                vec2(  
                    12.9898,  
                    78.233  
                )  
            )  
        )  
        * 43758.5453  
    );  

color +=  
    vec3(  
        0.65,  
        0.75,  
        0.85  
    )  
    * rain  
    * uRainIntensity  
    * 0.08;  

color +=  
    vec3(  
        0.9,  
        0.95,  
        1.0  
    )  
    * rain  
    * uSnowIntensity  
    * 0.12;  

fragColor =  
    vec4(  
        color,  
        texColor.a  
    );

}
"""

with open(os.path.join(shaders_dir, "panorama_360_environment.frag"), "w", encoding="utf-8") as f:
    f.write(advanced_shader_content)

# ============================================================
# 2. WORLD DEFINITIONS
# ============================================================

worlds_data = [
    (  
        "world_01_house_3d",  
        "WORLD_01_TITLE",  
        "CHAR_KA_PANYA",  
        ["AREA_LIVING", "AREA_BEDROOM", "AREA_DINING", "AREA_KITCHEN", "AREA_BALCONY"],  
        "cozy_house_ambient.ogg", "WARM_INDOOR", "SNEAK_TIPTOE", "TRIP_AND_LAUGH",  
        ["tip_toe_walk", "sniff_around", "giggle_comedy", "scratch_ear"],  
        "QUADRUPED_SMALL", 0.35  
    ),  
    (  
        "world_02_birds_360",  
        "WORLD_02_TITLE",  
        "CHAR_MAMA_NDEGE",  
        ["AREA_KUKU", "AREA_BATA", "AREA_KANGA", "AREA_MBUNI", "AREA_NJIWA"],  
        "farm_birds_chirping.ogg", "SUNNY_DAYLIGHT", "WOBBLE_STRUT", "WING_FLAP_DANCE",  
        ["wobble_walk", "peck_ground", "wing_shake_comedy", "squawk_talk"],  
        "BIPED_AVIAN", 0.45  
    ),  
    (  
        "world_03_cyber_city",  
        "WORLD_03_TITLE",  
        "CHAR_CYBER_DRONE",  
        ["AREA_MAIN_STREET", "AREA_ALLEY_LAB", "AREA_ROOFTOP", "AREA_CONTROL_CENTER", "AREA_SUBWAY"],  
        "cyber_synthwave.ogg", "NEON_NIGHT", "HOVER_GRID", "GLITCH_SPARK_DANCE",  
        ["hover_drift", "scan_user", "glitch_dance", "laser_wink"],  
        "HOVER_MECHA", 0.60  
    ),  
    (  
        "world_04_deep_ocean",  
        "WORLD_04_TITLE",  
        "CHAR_WHALE_GUARDIAN",  
        ["AREA_CORAL_REEF", "AREA_DEEP_TRENCH", "AREA_SUNKEN_SHIP", "AREA_CRYSTAL_CAVE", "AREA_ATLANTIS_GATE"],  
        "underwater_bubbles.ogg", "BIOLUMINESCENT_DEEP", "SWIM_FLOAT_WAVE", "WATER_BUBBLE_BLOW",  
        ["smooth_swim", "tail_flip", "bubble_pop_comedy", "deep_sing"],  
        "AQUATIC_SWIMMER", 0.80  
    ),  
    (  
        "world_05_volcano_lab",  
        "WORLD_05_TITLE",  
        "CHAR_MECHA_CORE",  
        ["AREA_CONTROL_DECK", "AREA_LAVA_PIT", "AREA_TURBINE_ROOM", "AREA_COOLING_BAY", "AREA_HELIPAD"],  
        "volcano_rumble.ogg", "MAGMA_GLOW", "HEAVY_MARCH", "STEAM_VENT_EXHAUST",  
        ["heavy_march", "arm_rotate", "steam_puff_comedy", "power_flex"],  
        "HEAVY_MECHA", 1.20  
    ),  
    (  
        "world_06_fantasy_island",  
        "WORLD_06_TITLE",  
        "CHAR_ANCIENT_DRAGON",  
        ["AREA_DRAGON_SHRINE", "AREA_SKY_BRIDGE", "AREA_CRYSTAL_CAVERN", "AREA_CLOUD_GARDEN", "AREA_HIGH_TOWER"],  
        "floating_wind_harp.ogg", "ETHEREAL_SKY", "HOVER_SWAY", "MINI_FIRE_SNEEZE",  
        ["glide_hover", "wing_fan", "fire_sneeze_comedy", "roar_soft"],  
        "SERPENTINE_DRAGON", 1.00  
    ),  
    (  
        "world_07_enchanted_forest",  
        "WORLD_07_TITLE",  
        "CHAR_SPIRIT_FOX",  
        ["AREA_GLOWING_TREE", "AREA_FAIRY_POND", "AREA_ELDER_SHRINE", "AREA_MUSHROOM_MEADOW", "AREA_DARK_CANOPY"],  
        "forest_magic_wind.ogg", "MYSTIC_GREEN", "NINJA_BOUND_LEAP", "TAIL_SPIN_MAGIC",  
        ["light_trot", "pounce_play", "tail_swish_comedy", "magic_sparkle"],  
        "QUADRUPED_AGILE", 0.40  
    ),  
    (  
        "world_08_space_station",  
        "WORLD_08_TITLE",  
        "CHAR_STATION_AI",  
        ["AREA_COMMAND_DECK", "AREA_ZERO_G_LAB", "AREA_AIRLOCK", "AREA_SOLAR_ARRAY", "AREA_OBSERVATION_DOME"],  
        "space_hum_engine.ogg", "ZERO_GRAVITY_BLUE", "ZERO_G_FLOAT", "GRAVITY_FLIP_COMEDY",  
        ["zero_g_drift", "spin_around", "antenna_twirl", "radar_ping"],  
        "ZERO_G_ORBITER", 0.50  
    ),  
    (  
        "world_09_desert_oasis",  
        "WORLD_09_TITLE",  
        "CHAR_ANUBIS_SENTINEL",  
        ["AREA_OASIS_CAMP", "AREA_PYRAMID_ENTRANCE", "AREA_TOMB_CHAMBER", "AREA_DUNE_VALLEY", "AREA_CARAVAN_MARKET"],  
        "desert_wind_flute.ogg", "GOLDEN_SUNSET", "REGAL_STRIDE", "SAND_MUMMY_SHAKE",  
        ["stately_walk", "staff_thump", "sand_sneeze_comedy", "sun_salute"],  
        "BIPED_CANINE", 0.70  
    ),  
    (  
        "world_10_arctic_palace",  
        "WORLD_10_TITLE",  
        "CHAR_SNOW_LEOPARD",  
        ["AREA_ICE_HALL", "AREA_CRYSTAL_CAVERN", "AREA_AURORA_BALCONY", "AREA_FROZEN_VAULT", "AREA_BLIZZARD_PEAK"],  
        "blizzard_wind_howl.ogg", "AURORA_BOREALIS", "ICE_SLIDE_BOUND", "FROZEN_SHIVER_JUMP",  
        ["prowl_walk", "ice_slide", "paw_lick_comedy", "frost_breath"],  
        "QUADRUPED_FELINE", 0.65  
    ),  
    (  
        "world_11_egypt_temple",  
        "WORLD_11_TITLE",  
        "CHAR_SPHINX_GUARD",  
        ["AREA_OUTER_COURT", "AREA_PILLAR_HALL", "AREA_INNER_SANCTUM", "AREA_TREASURE_CHAMBER", "AREA_ROYAL_GARDEN"],  
        "ancient_egypt_echo.ogg", "DESERT_NOON", "MARBLE_HEAVY_PAW", "GOLD_COIN_JUGGLE",  
        ["slow_prowl", "head_turn", "tail_flick_comedy", "roar_echo"],  
        "MYTHICAL_FELINE", 0.90  
    ),  
    (  
        "world_12_steampunk_factory",  
        "WORLD_12_TITLE",  
        "CHAR_STEAM_MASTER",  
        ["AREA_GEAR_ROOM", "AREA_FURNACE_PLATFORM", "AREA_PIPE_NETWORK", "AREA_CLOCK_TOWER", "AREA_AIRSHIP_DOCK"],  
        "steampunk_gears.ogg", "BRASS_INDUSTRIAL", "CLOCKWORK_JERK", "GEAR_POPS_LOOSE",  
        ["clockwork_stride", "wrench_spin", "gear_drop_comedy", "whistle_blow"],  
        "CLOCKWORK_AUTOMATON", 0.75  
    ),  
    (  
        "world_13_dinosaur_jungle",  
        "WORLD_13_TITLE",  
        "CHAR_TREX_LEADER",  
        ["AREA_DINO_NEST", "AREA_RIVER_CROSSING", "AREA_VOLCANO_EDGE", "AREA_WATERFALL_CAVE", "AREA_HIGH_CANOPY"],  
        "jungle_dino_roar.ogg", "TROPICAL_JUNGLE", "HEAVY_STOMP", "TINY_ARMS_SCRATCH",  
        ["heavy_stomp", "tail_sweep", "scratch_head_comedy", "loud_roar"],  
        "BIPED_REPTILIAN", 1.50  
    ),  
    (  
        "world_14_samurai_dojo",  
        "WORLD_14_TITLE",  
        "CHAR_MASTER_RONIN",  
        ["AREA_TRAINING_YARD", "AREA_ZEN_GARDEN", "AREA_ARMOR_VAULT", "AREA_CHERRY_BLOSSOM_PATH", "AREA_DOJO_PAVILION"],  
        "zen_bamboo_stream.ogg", "CHERRY_SUNRISE", "SHADOW_SLIDE", "KATANA_BALANCE_FAIL",  
        ["ninja_dash", "sword_sheathe", "balance_slip_comedy", "bow_respect"],  
        "HUMANOID_NINJA", 0.55  
    ),  
    (  
        "world_15_candyland_world",  
        "WORLD_15_TITLE",  
        "CHAR_GUMMY_BEAR_KING",  
        ["AREA_CHOCOLATE_RIVER", "AREA_CANDY_CASTLE", "AREA_LOLLIPOP_FOREST", "AREA_COOKIE_VILLAGE", "AREA_DONUT_HILLS"],  
        "candy_playful_tune.ogg", "SWEET_PASTEL", "BOUNCY_JELLY", "BELLY_RUB_LAUGH",  
        ["jelly_bounce", "belly_pat", "giggle_fit_comedy", "wave_hand"],  
        "AMORPHOUS_JELLY", 0.50  
    ),  
    (  
        "world_16_alien_hive",  
        "WORLD_16_TITLE",  
        "CHAR_HIVE_MOTHER",  
        ["AREA_SPORE_CHAMBER", "AREA_BIO_LAB", "AREA_QUEEN_THRONE", "AREA_TUNNEL_NETWORK", "AREA_SURFACE_CRATER"],  
        "alien_hive_resonance.ogg", "ALIEN_PURPLE", "MULTI_LEG_SKITTER", "SPORE_BURST_LAUGH",  
        ["skitter_crawl", "antenna_pulse", "spore_puff_comedy", "screech_tune"],  
        "INSECTOID_MULTI_LEG", 0.85  
    ),  
    (  
        "world_17_celestial_heaven",  
        "WORLD_17_TITLE",  
        "CHAR_ANGEL_SENTINEL",  
        ["AREA_GOLDEN_GATE", "AREA_CLOUD_GARDEN", "AREA_CRYSTAL_TEMPLE", "AREA_STAR_PLATFORM", "AREA_ETHEREAL_CROWN"],  
        "celestial_choir.ogg", "DIVINE_LIGHT", "DIVINE_LEVITATE", "HALO_RING_SPIN",  
        ["ethereal_float", "wing_spread", "halo_spin_comedy", "bless_wave"],  
        "CELESTIAL_WINGED", 0.60  
    )
]

# Helper Systems
def create_environment_control(world_id, preset, step_index):
    return {
        "environment_controller": {
            "enabled": True,
            "control_mode": "WORLD_AUTOMATIC_WITH_RUNTIME_OVERRIDE",
            "time_system": {
                "enabled": True, "cycle_mode": "CONTINUOUS",
                "day_duration_minutes": 18, "night_duration_minutes": 12,
                "current_phase": "AUTO", "allow_user_time_control": True
            },
            "weather_system": {
                "enabled": True,
                "available_modes": ["CLEAR", "CLOUDY", "RAIN", "STORM", "FOG", "SNOW", "MAGICAL_PARTICLES"],
                "selected_mode": "AUTO", "intensity": 0.35, "transition_seconds": 8.0
            },
            "wind_control": {"enabled": True, "speed": 1.5, "direction_degrees": 180.0, "gust_strength": 0.25, "dynamic_motion": True},
            "lighting_control": {"enabled": True, "preset": preset, "brightness": 1.0, "contrast": 1.0, "ambient_strength": 0.75, "bloom": 0.60, "dynamic_shadows": True, "shadow_quality": "HIGH"},
            "fog_control": {"enabled": True, "density": 0.15, "height_falloff": 0.50, "color_mode": "AUTO"},
            "particle_control": {"enabled": True, "max_particles": 150, "dynamic_spawn": True, "interaction_reaction": True},
            "environment_interaction": {"touch_reaction": True, "camera_reaction": True, "character_reaction": True, "wind_reaction": True, "sound_reaction": True}
        }
    }

def create_camera_system():
    return {
        "camera_system": {
            "mode": "360_FREE_SCROLL", "horizontal_rotation": 360.0, "vertical_rotation": 180.0,
            "smooth_scroll": True, "scroll_lerp_speed": 0.12, "touch_drag_enabled": True,
            "pinch_zoom_enabled": True, "double_tap_center": True, "auto_follow_leader": True,
            "camera_collision_protection": True, "camera_limits": {"minimum_pitch": -85.0, "maximum_pitch": 85.0}
        }
    }

def create_app_mount_system():
    return {
        "dynamic_app_mount_system": {
            "enabled": True, "selection_mode": "DEVICE_APP_PICKER", "multiple_slots": True,
            "replace_existing_app": True, "persistent_selection": True, "launch_selected_app": True,
            "return_to_world_after_close": True, "preserve_camera_position": True, "preserve_world_state": True,
            "app_slot_structure": {"package_name": "", "app_display_name": "", "app_icon_path": "", "app_version": "", "is_selected": False}
        }
    }

def create_persistence_system(world_id):
    return {
        "persistence_system": {
            "enabled": True, "storage_mode": "LOCAL_DEVICE", "world_state_key": f"STATE_{world_id}",
            "save_camera_position": True, "save_scroll_position": True, "save_environment_state": True,
            "save_selected_apps": True, "save_hotspot_states": True, "save_character_state": True,
            "restore_last_session": True, "auto_save": {"enabled": True, "interval_seconds": 15}
        }
    }

def create_event_system():
    return {
        "interaction_event_system": {
            "enabled": True,
            "events": {
                "on_world_enter": "RESTORE_WORLD_STATE", "on_world_exit": "SAVE_WORLD_STATE",
                "on_hotspot_tap": "ACTIVATE_HOTSPOT", "on_hotspot_long_press": "OPEN_APP_ACTION_MENU",
                "on_app_selected": "BIND_APP_TO_HOTSPOT", "on_environment_change": "UPDATE_ENVIRONMENT",
                "on_character_tap": "TRIGGER_CHARACTER_REACTION", "on_camera_move": "UPDATE_LEADER_FOLLOW",
                "on_scroll_step_change": "UPDATE_WORLD_SECTION"
            }
        }
    }

def create_performance_system():
    return {
        "performance_controller": {
            "target_fps": 60, "battery_saver_fps": 30, "ultra_mode": True, "adaptive_quality": True,
            "dynamic_lod": True, "texture_streaming": True, "particle_scaling": True, "shadow_scaling": True,
            "background_effect_reduction": True, "low_memory_protection": True, "thermal_protection": True
        }
    }

def create_external_ui_system():
    return {
        "external_ui_system": {
            "enabled": True, "startup_screen": "SYSTEM_HOME", "design_mode": "CLEAN_STABLE_MODERN", "layout_mode": "RESPONSIVE_ADAPTIVE",
            "navigation": {"type": "BOTTOM_AND_SIDE_PANEL", "home": True, "back": True, "search": True, "quick_controls": True},
            "main_sections": ["SYSTEM_HOME", "WORLD_BROWSER", "ANIMATIONS", "ENVIRONMENT", "DEVICE_CONTROLS", "BLUETOOTH_DEVICES", "WIFI_NETWORK", "HOTSPOT", "NOTIFICATIONS", "APPEARANCE", "PERFORMANCE", "AUDIO", "CAMERA", "STORAGE", "ABOUT"],
            "visual_layout": {"header": True, "status_summary": True, "large_action_cards": True, "compact_controls": True, "section_dividers": True, "animated_transitions": True, "smooth_scrolling": True, "responsive_touch": True},
            "theme": {"mode": "SYSTEM_DEFAULT", "available_modes": ["SYSTEM_DEFAULT", "LIGHT", "DARK"], "accent_color": "#6C63FF", "background_color": "#101218", "surface_color": "#181B22", "text_color": "#FFFFFF", "secondary_text_color": "#AEB4C0", "border_radius": 18, "transparency": 0.92, "font_scale": 1.0, "ui_scale": 1.0},
            "accessibility": {"large_text": True, "high_contrast": False, "reduce_motion": False, "haptic_feedback": True, "screen_reader_labels": True}
        }
    }

def create_master_power_system():
    return {
        "system_master_control": {
            "enabled": True, "system_state": "OFF", "startup_behavior": "ASK_USER_BEFORE_ACTIVATION", "user_confirmation_required": True,
            "activation_dialog": {"title_key": "SYSTEM_ACTIVATION_TITLE", "message_key": "SYSTEM_ACTIVATION_MESSAGE", "allow_button_key": "SYSTEM_ALLOW", "deny_button_key": "SYSTEM_DENY"},
            "controls": {"master_enable": True, "master_disable": True, "pause_system": True, "resume_system": True, "safe_mode": True},
            "when_disabled": {"stop_world_runtime": True, "stop_autonomous_ai": True, "stop_environment_animation": True, "stop_background_audio": True, "stop_dynamic_app_actions": True, "keep_ui_available": True, "show_reactivate_button": True},
            "safe_state": "UI_ONLY_NO_BACKGROUND_WORLD_RUNTIME"
        }
    }

def create_animation_library():
    return {
        "animation_system": {
            "enabled": True, "browser_screen": "ANIMATION_LIBRARY", "categories": ["MOVEMENT", "IDLE", "ACTION", "SOCIAL", "COMEDY", "REACTION", "CUSTOM"],
            "catalog": [
                {"animation_id": "ANIM_WALK", "title_key": "ANIMATION_WALK", "category": "MOVEMENT", "preview": True, "selectable": True, "apply_to": ["LEADER", "HOTSPOT_CREATURE"]},
                {"animation_id": "ANIM_RUN", "title_key": "ANIMATION_RUN", "category": "MOVEMENT", "preview": True, "selectable": True, "apply_to": ["LEADER", "HOTSPOT_CREATURE"]},
                {"animation_id": "ANIM_IDLE", "title_key": "ANIMATION_IDLE", "category": "IDLE", "preview": True, "selectable": True, "apply_to": ["LEADER", "HOTSPOT_CREATURE"]},
                {"animation_id": "ANIM_JUMP", "title_key": "ANIMATION_JUMP", "category": "ACTION", "preview": True, "selectable": True, "apply_to": ["LEADER", "HOTSPOT_CREATURE"]},
                {"animation_id": "ANIM_DANCE", "title_key": "ANIMATION_DANCE", "category": "COMEDY", "preview": True, "selectable": True, "apply_to": ["LEADER", "HOTSPOT_CREATURE"]}
            ],
            "controls": {"play": True, "pause": True, "stop": True, "loop": True, "speed": True, "preview": True, "apply": True, "reset": True},
            "speed_range": {"minimum": 0.25, "maximum": 2.0, "default": 1.0}
        }
    }

def create_device_control_center():
    return {
        "device_control_center": {
            "enabled": True, "mode": "ANDROID_SYSTEM_INTEGRATION",
            "sections": {
                "connectivity": {"wifi": {"enabled": True, "open_system_settings": True, "action": "OPEN_WIFI_SETTINGS"}, "bluetooth": {"enabled": True, "open_system_settings": True, "request_enable": True, "action": "OPEN_BLUETOOTH_SETTINGS"}},
                "display": {"brightness": "SYSTEM_CONTROL_OR_SETTINGS", "dark_mode": True},
                "sound": {"media_volume": "SYSTEM_SETTINGS"},
                "battery": {"battery_status": "READ_ONLY"}
            }
        }
    }

def create_bluetooth_multi_device_system():
    return {
        "bluetooth_multi_device_manager": {
            "enabled": True, "requested_device_slots": 4, "maximum_slots": 4, "capability_detection": True,
            "device_slots": [{"slot": i, "enabled": True, "device_id": "", "device_name": "", "connection_state": "DISCONNECTED"} for i in range(1, 5)]
        }
    }

def create_network_system():
    return {"network_control_system": {"enabled": True, "wifi": {"scan": True, "open_wifi_settings": True}, "hotspot": {"enabled": True, "open_hotspot_settings": True}}}

def create_device_monitor():
    return {"device_monitor": {"enabled": True, "information": {"android_version": "READ_ONLY", "device_model": "READ_ONLY"}, "runtime_monitor": {"fps": True, "memory_usage": True}}}

def create_appearance_system():
    return {"appearance_system": {"enabled": True, "theme_modes": ["SYSTEM_DEFAULT", "LIGHT", "DARK"], "color_controls": {"accent": "#6C63FF", "background": "#101218", "surface": "#181B22", "text": "#FFFFFF"}}}

def create_quick_control_panel():
    return {"quick_control_panel": {"enabled": True, "layout": "COMPACT_GRID", "items": [{"id": "MASTER_SYSTEM", "type": "TOGGLE", "action": "TOGGLE_SYSTEM"}]}}

# ============================================================
# 3. GENERATE ALL JSON WORLDS
# ============================================================

for index, (w_id, title_key, char_key, sub_area_keys, amb_sound, preset, walk_style, comedy, anim_list, body_type, weight_limit) in enumerate(worlds_data, start=1):
    steps_data = []
    for step_idx, area_key in enumerate(sub_area_keys, start=1):
        hotspots = []
        for h_id in range(1, 81):
            base_x = round(((h_id % 10) - 4.5) * 0.6, 3)
            base_y = round(((h_id // 10) - 3.5) * 0.5, 3)
            base_z = round(-3.5 - (h_id % 3) * 0.2, 3)

            hotspot = {
                "hotspot_id": f"H_S{step_idx}_{h_id:02d}",
                "node_label_key": "TRAP_NODE_LABEL",
                "save_state_key": f"{w_id}_step_{step_idx}_slot_{h_id}",
                "physics_collision": {"enabled": True, "bounding_box_radius": 0.45, "physics_response": "DYNAMIC"},
                "transform_3d": {"position_x": base_x, "position_y": base_y, "position_z": base_z, "rotation_x": 0.0, "rotation_y": round((h_id * 4.5) % 360, 2), "rotation_z": 0.0, "scale": round(0.85 + (h_id % 4) * 0.05, 2)},
                "autonomous_creature_ai": {
                    "is_independent_entity": True, "body_structure_type": body_type,
                    "locomotion_kinematics": {"gait_type": walk_style, "walk_speed": round(0.5 + (h_id % 5) * 0.2, 2), "stride_length": 0.35, "ground_impact_weight": weight_limit},
                    "comedy_and_behavior": {"primary_comedy_action": comedy, "idle_routine_list": anim_list}
                },
                "back_mount_payload": {"enabled": True, "attachment_node": "spine_back_mount_joint", "max_weight_capacity_kg": weight_limit, "mounting_offset": {"x": 0.0, "y": 0.15, "z": 0.05}, "mounting_rotation_y": 180.0, "ui_label_key": "LABEL_MOUNT_APP_BACK", "scale": 1.0},
                "spatial_audio": {"enabled": True, "sound_effect": f"sfx_trap_click_{h_id % 5}.wav"},
                "stealth_app_link": {"is_active": False, "package_name": "", "action": "LAUNCH_DEVICE_APP_PICKER"},
                "interaction": {"tap_enabled": True, "long_press_enabled": True}
            }
            hotspots.append(hotspot)

        steps_data.append({
            "scroll_step_index": step_idx, "sub_area_key": area_key,
            "camera_yaw_rotation": (step_idx - 1) * 72.0, "camera_pitch_tilt": -2.5 if step_idx % 2 == 0 else 0.0,
            "hotspots_count": 80, "hotspots": hotspots, "environment": create_environment_control(w_id, preset, step_idx)
        })

    world_json = {
        "world_index": index, "world_id": w_id, "world_title_key": title_key, "world_version": "2.0",
        "world_status": "READY", "render_quality": "8K_EXTREME_ULTRA_HD", "render_engine": "PANORAMA_360_ENVIRONMENT",
        "performance_settings": {"enable_lod": True, "target_fps": 60, "battery_saver_mode_fps": 30},
        "living_environment_effects": {"background_ambient_soundtrack": amb_sound, "volume_db": -6.0, "3d_reverb_preset": preset},
        "main_leader_entity": {
            "name_key": char_key, "role": "MAIN_MENU_TRIGGER_AND_PERSISTENCE_FOLLOWER",
            "autonomous_ai": {"body_structure_type": body_type, "locomotion_kinematics": {"gait_type": walk_style, "walk_speed": 1.0}, "comedy_personality": {"signature_comedy_move": comedy, "idle_animation_set": anim_list}},
            "back_mount_payload": {"enabled": True, "attachment_node": "main_leader_back_joint", "max_weight_capacity_kg": weight_limit * 1.5}
        },
        "scroll_system": {"total_scroll_steps": 5, "steps": steps_data},
        "systems": {
            "camera": create_camera_system(), "app_mount": create_app_mount_system(), "persistence": create_persistence_system(w_id),
            "interaction": create_event_system(), "performance": create_performance_system(), "external_ui": create_external_ui_system(),
            "master_power": create_master_power_system(), "animation_library": create_animation_library(), "device_control": create_device_control_center(),
            "bluetooth_manager": create_bluetooth_multi_device_system(), "network_control": create_network_system(), "device_monitor": create_device_monitor(),
            "appearance": create_appearance_system(), "quick_control": create_quick_control_panel()
        }
    }

    world_file = os.path.join(worlds_dir, f"{w_id}.json")
    with open(world_file, "w", encoding="utf-8") as f:
        json.dump(world_json, f, indent=2, ensure_ascii=False)

# Config & Locales
environment_master = {"environment_system_version": "2.0", "controller": "CENTRAL_RUNTIME_ENVIRONMENT_CONTROLLER", "runtime_control": True}
with open(os.path.join(config_dir, "environment_controller.json"), "w", encoding="utf-8") as f:
    json.dump(environment_master, f, indent=2)

swahili_translations = {"LABEL_MOUNT_APP_BACK": "Weka App Hapa Mgongoni", "TRAP_NODE_LABEL": "Mtego wa App", "SYSTEM_ACTIVATION_TITLE": "Washa Mfumo"}
with open(os.path.join(locales_dir, "strings_sw.json"), "w", encoding="utf-8") as f:
    json.dump(swahili_translations, f, indent=2, ensure_ascii=False)

master_manifest = {"system_name": "LIVING_360_WORLD_ENGINE", "system_version": "2.0", "world_count": len(worlds_data), "default_world": "world_01_house_3d"}
with open(os.path.join(config_dir, "master_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(master_manifest, f, indent=2, ensure_ascii=False)

# ============================================================
# 4. GENERATE ENGINE ARCHITECTURE DOCUMENTATION
# ============================================================

doc_content = """# LIVING 360 WORLD ENGINE & UI SYSTEM
## TECHNICAL ARCHITECTURE & GRAPHICS SPECIFICATION GUIDE FOR ENGINEERS

---

## 1. Mfumo wa UI na Architecture (Server-Driven / JSON-Driven Mobile Interfaces)
Mfumo huu umejengwa kwa kutumia muundo wa **JSON-Driven UI (SDUI)** ambapo mambo yote ya mionekano, mienendo, rangi, na animation hayatokani na code iliyokuwa 'hardcoded' bali yanasomwa moja kwa moja kutoka kwenye JSON Schemas za kila Dunia na Master Manifest.

### Majukumu ya Engineer wakati wa Kuunda Injini:
1. **JSON Parser & Runtime Renderer:** Injini inatakiwa kusoma files za `.json` zilizomo kwenye `assets/worlds/` na `assets/config/` ili kutengeneza Graphics Pipeline, Lightings, na Entities kwa muda huo huo (Real-Time).
2. **State Management & Persistence:** Kila mabadiliko ya kamera, hotspot iliyobadilishwa app, au mazingira yanahifadhiwa kwenye Local Device Database kupitia funguo za `STATE_world_id`.

---

## 2. OpenGL ES 3.0 Environment Shader Pipeline
Shader inayotumika kwenye mazingira 360 (`panorama_360_environment.frag`) ina vigezo vifuatavyo vya kiufundi:
* **uPanoramaTexture (sampler2D):** Picha ya Panorama 360° inayofunika mazingira.
* **uYawAngle / uPitchAngle (float):** Mzunguko wa kamera (-85.0 hadi 85.0 Pitch, 0 hadi 360 Yaw).
* **uColorFilter (vec3):** Filter ya rangi za mazingira kulingana na Theme ya Dunia.

---

## 3. Uchambuzi wa Dunia zote 17 (Worlds Blueprint & Rendering Details)
"""

for idx, item in enumerate(worlds_data, start=1):
    w_id, title, char_k, sub_areas, amb, preset, walk, comedy, anims, body, weight = item
    doc_content += f"""
### Dunia {idx:02d}: {w_id}
* **Jina:** {title} | **Mhusika Mkuu:** {char_k} (Body: `{body}`, Uzito: {weight}kg)
* **Sub-Areas ({len(sub_areas)}):** {', '.join(sub_areas)}
* **Preset ya Mwanga:** `{preset}` | **Sauti:** `{amb}`
* **Animations:** {', '.join(anims)}
"""

with open(os.path.join(docs_dir, "engine_architecture_doc.md"), "w", encoding="utf-8") as f:
    f.write(doc_content)

print("")
print("=======================================================")
print(" SUCCESS! ALL ASSETS & DOCUMENTATION CREATED! ")
print("=======================================================")
print(" 1. Shaders: assets/shaders/panorama_360_environment.frag")
print(" 2. Worlds: 17 JSON files created in assets/worlds/")
print(" 3. Configs: Created in assets/config/ & assets/locales/")
print(" 4. Documentation: docs/engine_architecture_doc.md")
print("=======================================================")
print("")
