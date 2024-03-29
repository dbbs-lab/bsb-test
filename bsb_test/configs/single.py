required_plugins = []

tree = {
    "storage": {"engine": "fs"},
    "network": {"x": 150.0, "y": 150.0, "z": 150.0, "chunk_size": [150, 150, 150]},
    "regions": {"test_region": {"children": ["test_layer"]}},
    "partitions": {"test_layer": {"thickness": 100.0}},
    "cell_types": {
        "test_cell": {
            "spatial": {"radius": 2.5, "count": 40},
            "plotting": {"display_name": "lonely cell", "color": "#E62214"},
        }
    },
    "placement": {
        "test_placement": {
            "strategy": "bsb.placement.RandomPlacement",
            "partitions": ["test_layer"],
            "cell_types": ["test_cell"],
        }
    },
    "connectivity": {},
    "simulations": {},
}
