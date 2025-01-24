# Connection parameters
import os
wcs_url = 'https://www.geo.euskadi.eus/WCS_KARTOGRAFIA'
wms_url = 'https://www.geo.euskadi.eus/WMS_ORTOARGAZKIAK?"'
current_dir = os.path.dirname(os.path.abspath("__file__"))
services_dir = os.path.abspath(os.path.join(current_dir, ".."))
output_dir = os.path.join(services_dir, "outputs")
input_file = os.path.join(services_dir, "input", "azkoitia.geojson")
tiles_dir = os.path.join(output_dir, "tiles")