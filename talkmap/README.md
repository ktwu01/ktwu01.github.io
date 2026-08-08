# Talkmap Feature

## Overview
The talkmap feature automatically generates an interactive map showing all the locations where you've given talks and presentations. The map is embedded directly in the `/talks/` page.

## How It Works

1. **Talk Metadata**: Each talk file in `_talks/` contains location information in its YAML frontmatter:
   ```yaml
   ---
   title: "Your Talk Title"
   venue: "Conference Name"
   location: "City, State/Country"
   ---
   ```

2. **Map Generation**: The `talkmap.py` script (or `talkmap.ipynb` Jupyter notebook) reads all talk files, geocodes the locations, and generates:
   - `talkmap/org-locations.js` - JavaScript file with geocoded coordinates
   - `talkmap/map.html` - Interactive Leaflet map

3. **Display**: The map is embedded in `_pages/talks.html` using an iframe.

## Regenerating the Map

When you add new talks or update locations, regenerate the map:

### Option 1: Using Python Script
```bash
python3 talkmap.py
```

### Option 2: Using Jupyter Notebook
```bash
jupyter nbconvert --to notebook --execute talkmap.ipynb --output talkmap_out.ipynb
```

### Prerequisites
Install required dependencies:
```bash
pip install python-frontmatter getorg geopy --upgrade
```

## Troubleshooting

### SSL Certificate Errors
If you encounter SSL certificate verification errors when running the script, you may need to:
1. Install/update certificates on your system
2. Or manually update the `talkmap/org-locations.js` file with coordinates

### Finding Coordinates
You can manually find coordinates for locations at:
- https://www.latlong.net/
- https://nominatim.openstreetmap.org/

Then update `talkmap/org-locations.js` in this format:
```javascript
var addressPoints = [
    [latitude, longitude, "Talk Title<br />Venue; Location"],
    // ... more entries
];
```

## Files Structure

- `_talks/*.md` - Individual talk files with location metadata
- `talkmap.py` - Python script to generate the map
- `talkmap.ipynb` - Jupyter notebook version
- `talkmap/map.html` - The interactive map HTML
- `talkmap/org-locations.js` - Geocoded location data
- `talkmap/leaflet_dist/` - Leaflet library files
- `_pages/talks.html` - Talks page with embedded map

## Features

- **Interactive Clustering**: Nearby locations are automatically clustered
- **Responsive Design**: Map adapts to different screen sizes
- **Automatic Updates**: Just run the script after adding new talks
- **No Separate Page**: Map is integrated directly into the talks page
