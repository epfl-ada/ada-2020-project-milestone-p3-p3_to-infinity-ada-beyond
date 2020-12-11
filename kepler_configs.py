config_nyc = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "NYC Data"
          ],
          "id": "1k2kprcyk",
          "name": [
            "time"
          ],
          "type": "timeRange",
          "value": [
            1608933741820.963,
            1608937388820.9624
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "r3qzh0k",
          "type": "geojson",
          "config": {
            "dataId": "NYC Data",
            "label": "NYC Data",
            "color": [
              50,
              26,
              151
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 0.41,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": None,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "c6mmjam",
          "type": "heatmap",
          "config": {
            "dataId": "NYC Data",
            "label": "heatmap",
            "color": [
              137,
              218,
              193
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.6,
              "colorRange": {
                "name": "UberPool 6",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#213E9A",
                  "#551EAD",
                  "#C019BD",
                  "#D31256",
                  "#E6470A",
                  "#F9E200"
                ]
              },
              "radius": 5
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "weightField": None,
            "weightScale": "linear"
          }
        },
        {
          "id": "2m5lxn",
          "type": "hexagon",
          "config": {
            "dataId": "NYC Data",
            "label": "3d map",
            "color": [
              221,
              178,
              124
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 0.8,
              "worldUnitSize": 0.3,
              "resolution": 8,
              "colorRange": {
                "name": "ColorBrewer GnBu-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f0f9e8",
                  "#ccebc5",
                  "#a8ddb5",
                  "#7bccc4",
                  "#43a2ca",
                  "#0868ac"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                500
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 10,
              "colorAggregation": "count",
              "sizeAggregation": "count",
              "enable3d": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "NYC Data": [
              {
                "name": "level_0",
                "format": None
              },
              {
                "name": "index",
                "format": None
              },
              {
                "name": "user_ID",
                "format": None
              },
              {
                "name": "venue_ID",
                "format": None
              },
              {
                "name": "venue_category_ID",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": False
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": -4.747252747252755,
      "dragRotate": True,
      "latitude": 40.692747044182674,
      "longitude": -73.93701669776497,
      "pitch": 47.00944974415832,
      "zoom": 9.620163690018412,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}



config_tky = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "TKY Data"
          ],
          "id": "1k2kprcyk",
          "name": [
            "time"
          ],
          "type": "timeRange",
          "value": [
            1608856298596.051,
            1608859945596.0513
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "free",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "r3qzh0k",
          "type": "geojson",
          "config": {
            "dataId": "TKY Data",
            "label": "TKY Data",
            "color": [
              50,
              26,
              151
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.41,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                255,
                254,
                230
              ],
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": True,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        },
        {
          "id": "c6mmjam",
          "type": "heatmap",
          "config": {
            "dataId": "TKY Data",
            "label": "heatmap",
            "color": [
              137,
              218,
              193
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 0.6,
              "colorRange": {
                "name": "UberPool 6",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#213E9A",
                  "#551EAD",
                  "#C019BD",
                  "#D31256",
                  "#E6470A",
                  "#F9E200"
                ]
              },
              "radius": 5
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "weightField": None,
            "weightScale": "linear"
          }
        },
        {
          "id": "2m5lxn",
          "type": "hexagon",
          "config": {
            "dataId": "TKY Data",
            "label": "3d map",
            "color": [
              221,
              178,
              124
            ],
            "columns": {
              "lat": "latitude",
              "lng": "longitude"
            },
            "isVisible": False,
            "visConfig": {
              "opacity": 0.3,
              "worldUnitSize": 0.3,
              "resolution": 8,
              "colorRange": {
                "name": "ColorBrewer GnBu-6",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#f0f9e8",
                  "#ccebc5",
                  "#a8ddb5",
                  "#7bccc4",
                  "#43a2ca",
                  "#0868ac"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                500
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 10,
              "colorAggregation": "count",
              "sizeAggregation": "count",
              "enable3d": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "TKY Data": [
              {
                "name": "user_ID",
                "format": None
              },
              {
                "name": "venue_ID",
                "format": None
              },
              {
                "name": "venue_category_ID",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": False
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": -8.55114116652579,
      "dragRotate": True,
      "latitude": 35.662258911895144,
      "longitude": 139.74505911325818,
      "pitch": 51.120658737628666,
      "zoom": 10.860491070055236,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        218.82023004728686,
        223.47597962276103,
        223.47597962276103
      ],
      "mapStyles": {}
    }
  }
}