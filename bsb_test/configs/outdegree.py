required_plugins = []

tree = {
    "storage": {"engine": "fs"},
    "network": {"x": 150.0, "y": 150.0, "z": 150.0},
    "partitions": {"all": {"type": "layer", "thickness": 150.0}},
    "cell_types": {
        "inhibitory": {"spatial": {"radius": 1.0, "count": 2000}},
        "excitatory": {"spatial": {"radius": 1.0, "count": 2000}},
        "extra": {"spatial": {"radius": 1.0, "count": 2000}},
    },
    "placement": {
        "random": {
            "strategy": "bsb.placement.RandomPlacement",
            "cell_types": ["inhibitory", "excitatory", "extra"],
            "partitions": ["all"],
        }
    },
    "connectivity": {
        "outdegree": {
            "strategy": "bsb.connectivity.FixedOutdegree",
            "outdegree": 50,
            "presynaptic": {"cell_types": ["excitatory"]},
            "postsynaptic": {"cell_types": ["inhibitory"]},
        },
        "multi_outdegree": {
            "strategy": "bsb.connectivity.FixedOutdegree",
            "outdegree": 50,
            "presynaptic": {"cell_types": ["excitatory", "extra"]},
            "postsynaptic": {"cell_types": ["inhibitory", "extra"]},
        },
    },
    "simulations": {},
}
