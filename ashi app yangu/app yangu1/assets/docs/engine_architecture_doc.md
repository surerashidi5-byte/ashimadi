# LIVING 360 WORLD ENGINE & UI SYSTEM
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

### Dunia 01: world_01_house_3d
* **Jina:** WORLD_01_TITLE | **Mhusika Mkuu:** CHAR_KA_PANYA (Body: `QUADRUPED_SMALL`, Uzito: 0.35kg)
* **Sub-Areas (5):** AREA_LIVING, AREA_BEDROOM, AREA_DINING, AREA_KITCHEN, AREA_BALCONY
* **Preset ya Mwanga:** `WARM_INDOOR` | **Sauti:** `cozy_house_ambient.ogg`
* **Animations:** tip_toe_walk, sniff_around, giggle_comedy, scratch_ear

### Dunia 02: world_02_birds_360
* **Jina:** WORLD_02_TITLE | **Mhusika Mkuu:** CHAR_MAMA_NDEGE (Body: `BIPED_AVIAN`, Uzito: 0.45kg)
* **Sub-Areas (5):** AREA_KUKU, AREA_BATA, AREA_KANGA, AREA_MBUNI, AREA_NJIWA
* **Preset ya Mwanga:** `SUNNY_DAYLIGHT` | **Sauti:** `farm_birds_chirping.ogg`
* **Animations:** wobble_walk, peck_ground, wing_shake_comedy, squawk_talk

### Dunia 03: world_03_cyber_city
* **Jina:** WORLD_03_TITLE | **Mhusika Mkuu:** CHAR_CYBER_DRONE (Body: `HOVER_MECHA`, Uzito: 0.6kg)
* **Sub-Areas (5):** AREA_MAIN_STREET, AREA_ALLEY_LAB, AREA_ROOFTOP, AREA_CONTROL_CENTER, AREA_SUBWAY
* **Preset ya Mwanga:** `NEON_NIGHT` | **Sauti:** `cyber_synthwave.ogg`
* **Animations:** hover_drift, scan_user, glitch_dance, laser_wink

### Dunia 04: world_04_deep_ocean
* **Jina:** WORLD_04_TITLE | **Mhusika Mkuu:** CHAR_WHALE_GUARDIAN (Body: `AQUATIC_SWIMMER`, Uzito: 0.8kg)
* **Sub-Areas (5):** AREA_CORAL_REEF, AREA_DEEP_TRENCH, AREA_SUNKEN_SHIP, AREA_CRYSTAL_CAVE, AREA_ATLANTIS_GATE
* **Preset ya Mwanga:** `BIOLUMINESCENT_DEEP` | **Sauti:** `underwater_bubbles.ogg`
* **Animations:** smooth_swim, tail_flip, bubble_pop_comedy, deep_sing

### Dunia 05: world_05_volcano_lab
* **Jina:** WORLD_05_TITLE | **Mhusika Mkuu:** CHAR_MECHA_CORE (Body: `HEAVY_MECHA`, Uzito: 1.2kg)
* **Sub-Areas (5):** AREA_CONTROL_DECK, AREA_LAVA_PIT, AREA_TURBINE_ROOM, AREA_COOLING_BAY, AREA_HELIPAD
* **Preset ya Mwanga:** `MAGMA_GLOW` | **Sauti:** `volcano_rumble.ogg`
* **Animations:** heavy_march, arm_rotate, steam_puff_comedy, power_flex

### Dunia 06: world_06_fantasy_island
* **Jina:** WORLD_06_TITLE | **Mhusika Mkuu:** CHAR_ANCIENT_DRAGON (Body: `SERPENTINE_DRAGON`, Uzito: 1.0kg)
* **Sub-Areas (5):** AREA_DRAGON_SHRINE, AREA_SKY_BRIDGE, AREA_CRYSTAL_CAVERN, AREA_CLOUD_GARDEN, AREA_HIGH_TOWER
* **Preset ya Mwanga:** `ETHEREAL_SKY` | **Sauti:** `floating_wind_harp.ogg`
* **Animations:** glide_hover, wing_fan, fire_sneeze_comedy, roar_soft

### Dunia 07: world_07_enchanted_forest
* **Jina:** WORLD_07_TITLE | **Mhusika Mkuu:** CHAR_SPIRIT_FOX (Body: `QUADRUPED_AGILE`, Uzito: 0.4kg)
* **Sub-Areas (5):** AREA_GLOWING_TREE, AREA_FAIRY_POND, AREA_ELDER_SHRINE, AREA_MUSHROOM_MEADOW, AREA_DARK_CANOPY
* **Preset ya Mwanga:** `MYSTIC_GREEN` | **Sauti:** `forest_magic_wind.ogg`
* **Animations:** light_trot, pounce_play, tail_swish_comedy, magic_sparkle

### Dunia 08: world_08_space_station
* **Jina:** WORLD_08_TITLE | **Mhusika Mkuu:** CHAR_STATION_AI (Body: `ZERO_G_ORBITER`, Uzito: 0.5kg)
* **Sub-Areas (5):** AREA_COMMAND_DECK, AREA_ZERO_G_LAB, AREA_AIRLOCK, AREA_SOLAR_ARRAY, AREA_OBSERVATION_DOME
* **Preset ya Mwanga:** `ZERO_GRAVITY_BLUE` | **Sauti:** `space_hum_engine.ogg`
* **Animations:** zero_g_drift, spin_around, antenna_twirl, radar_ping

### Dunia 09: world_09_desert_oasis
* **Jina:** WORLD_09_TITLE | **Mhusika Mkuu:** CHAR_ANUBIS_SENTINEL (Body: `BIPED_CANINE`, Uzito: 0.7kg)
* **Sub-Areas (5):** AREA_OASIS_CAMP, AREA_PYRAMID_ENTRANCE, AREA_TOMB_CHAMBER, AREA_DUNE_VALLEY, AREA_CARAVAN_MARKET
* **Preset ya Mwanga:** `GOLDEN_SUNSET` | **Sauti:** `desert_wind_flute.ogg`
* **Animations:** stately_walk, staff_thump, sand_sneeze_comedy, sun_salute

### Dunia 10: world_10_arctic_palace
* **Jina:** WORLD_10_TITLE | **Mhusika Mkuu:** CHAR_SNOW_LEOPARD (Body: `QUADRUPED_FELINE`, Uzito: 0.65kg)
* **Sub-Areas (5):** AREA_ICE_HALL, AREA_CRYSTAL_CAVERN, AREA_AURORA_BALCONY, AREA_FROZEN_VAULT, AREA_BLIZZARD_PEAK
* **Preset ya Mwanga:** `AURORA_BOREALIS` | **Sauti:** `blizzard_wind_howl.ogg`
* **Animations:** prowl_walk, ice_slide, paw_lick_comedy, frost_breath

### Dunia 11: world_11_egypt_temple
* **Jina:** WORLD_11_TITLE | **Mhusika Mkuu:** CHAR_SPHINX_GUARD (Body: `MYTHICAL_FELINE`, Uzito: 0.9kg)
* **Sub-Areas (5):** AREA_OUTER_COURT, AREA_PILLAR_HALL, AREA_INNER_SANCTUM, AREA_TREASURE_CHAMBER, AREA_ROYAL_GARDEN
* **Preset ya Mwanga:** `DESERT_NOON` | **Sauti:** `ancient_egypt_echo.ogg`
* **Animations:** slow_prowl, head_turn, tail_flick_comedy, roar_echo

### Dunia 12: world_12_steampunk_factory
* **Jina:** WORLD_12_TITLE | **Mhusika Mkuu:** CHAR_STEAM_MASTER (Body: `CLOCKWORK_AUTOMATON`, Uzito: 0.75kg)
* **Sub-Areas (5):** AREA_GEAR_ROOM, AREA_FURNACE_PLATFORM, AREA_PIPE_NETWORK, AREA_CLOCK_TOWER, AREA_AIRSHIP_DOCK
* **Preset ya Mwanga:** `BRASS_INDUSTRIAL` | **Sauti:** `steampunk_gears.ogg`
* **Animations:** clockwork_stride, wrench_spin, gear_drop_comedy, whistle_blow

### Dunia 13: world_13_dinosaur_jungle
* **Jina:** WORLD_13_TITLE | **Mhusika Mkuu:** CHAR_TREX_LEADER (Body: `BIPED_REPTILIAN`, Uzito: 1.5kg)
* **Sub-Areas (5):** AREA_DINO_NEST, AREA_RIVER_CROSSING, AREA_VOLCANO_EDGE, AREA_WATERFALL_CAVE, AREA_HIGH_CANOPY
* **Preset ya Mwanga:** `TROPICAL_JUNGLE` | **Sauti:** `jungle_dino_roar.ogg`
* **Animations:** heavy_stomp, tail_sweep, scratch_head_comedy, loud_roar

### Dunia 14: world_14_samurai_dojo
* **Jina:** WORLD_14_TITLE | **Mhusika Mkuu:** CHAR_MASTER_RONIN (Body: `HUMANOID_NINJA`, Uzito: 0.55kg)
* **Sub-Areas (5):** AREA_TRAINING_YARD, AREA_ZEN_GARDEN, AREA_ARMOR_VAULT, AREA_CHERRY_BLOSSOM_PATH, AREA_DOJO_PAVILION
* **Preset ya Mwanga:** `CHERRY_SUNRISE` | **Sauti:** `zen_bamboo_stream.ogg`
* **Animations:** ninja_dash, sword_sheathe, balance_slip_comedy, bow_respect

### Dunia 15: world_15_candyland_world
* **Jina:** WORLD_15_TITLE | **Mhusika Mkuu:** CHAR_GUMMY_BEAR_KING (Body: `AMORPHOUS_JELLY`, Uzito: 0.5kg)
* **Sub-Areas (5):** AREA_CHOCOLATE_RIVER, AREA_CANDY_CASTLE, AREA_LOLLIPOP_FOREST, AREA_COOKIE_VILLAGE, AREA_DONUT_HILLS
* **Preset ya Mwanga:** `SWEET_PASTEL` | **Sauti:** `candy_playful_tune.ogg`
* **Animations:** jelly_bounce, belly_pat, giggle_fit_comedy, wave_hand

### Dunia 16: world_16_alien_hive
* **Jina:** WORLD_16_TITLE | **Mhusika Mkuu:** CHAR_HIVE_MOTHER (Body: `INSECTOID_MULTI_LEG`, Uzito: 0.85kg)
* **Sub-Areas (5):** AREA_SPORE_CHAMBER, AREA_BIO_LAB, AREA_QUEEN_THRONE, AREA_TUNNEL_NETWORK, AREA_SURFACE_CRATER
* **Preset ya Mwanga:** `ALIEN_PURPLE` | **Sauti:** `alien_hive_resonance.ogg`
* **Animations:** skitter_crawl, antenna_pulse, spore_puff_comedy, screech_tune

### Dunia 17: world_17_celestial_heaven
* **Jina:** WORLD_17_TITLE | **Mhusika Mkuu:** CHAR_ANGEL_SENTINEL (Body: `CELESTIAL_WINGED`, Uzito: 0.6kg)
* **Sub-Areas (5):** AREA_GOLDEN_GATE, AREA_CLOUD_GARDEN, AREA_CRYSTAL_TEMPLE, AREA_STAR_PLATFORM, AREA_ETHEREAL_CROWN
* **Preset ya Mwanga:** `DIVINE_LIGHT` | **Sauti:** `celestial_choir.ogg`
* **Animations:** ethereal_float, wing_spread, halo_spin_comedy, bless_wave
