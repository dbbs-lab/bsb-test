required_plugins = []

tree = {
    "storage": {"engine": "fs"},
    "network": {"x": 100, "y": 100, "z": 50},
    "partitions": {},
    "cell_types": {
        "A": {
            "spatial": {"count": 1},
        },
        "B": {
            "spatial": {"count": 1},
        },
        "C": {
            "spatial": {"count": 1},
        },
    },
    "placement": {
        "across_chunks": {
            "strategy": "bsb.placement.FixesPosPlacement",
            "cell_types": ["A", "B", "C"],
            "partitions": [],
            "positions": [
                [10, 10, 10],
                [20, 10, 10],
                [30, 10, 10],
                [60, 10, 10],
                [70, 10, 10],
                [80, 10, 10],
                [10, 60, 10],
                [10, 70, 10],
                [10, 80, 10],
                [60, 60, 10],
                [70, 70, 10],
                [80, 80, 10],
            ],
        }
    },
    "connectivity": {""},
    "simulations": {},
}
