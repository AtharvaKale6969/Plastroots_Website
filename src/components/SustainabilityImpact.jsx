import React, { useState } from 'react';
import * as SimpleMaps from 'react-simple-maps';
import { geoCentroid } from 'd3-geo';
import CountUpLib from 'react-countup';

const CountUp = CountUpLib.default || CountUpLib;
const { ComposableMap, Geographies, Geography, Marker } = SimpleMaps.default || SimpleMaps;
const geoUrl = "/india-states.json";

const activeStates = [
    "Maharashtra", "Madhya Pradesh", "Telangana", "Karnataka", "Tamil Nadu", 
    "Goa", "Odisha", "Jharkhand", "Uttar Pradesh", "Bihar", "Uttarakhand", 
    "Gujarat", "Rajasthan", "Punjab", "Himachal Pradesh", "Jammu and Kashmir", 
    "Delhi", "Assam", "Nagaland"
];

const formatStateName = (name) => {
    if (name === "Jammu and Kashmir") return ["Jammu &", "Kashmir"];
    if (name === "Madhya Pradesh") return ["Madhya", "Pradesh"];
    if (name === "Uttar Pradesh") return ["Uttar", "Pradesh"];
    if (name === "Himachal Pradesh") return ["Himachal", "Pradesh"];
    if (name === "Andhra Pradesh") return ["Andhra", "Pradesh"];
    if (name === "Arunachal Pradesh") return ["Arunachal", "Pradesh"];
    if (name === "Tamil Nadu") return ["Tamil", "Nadu"];
    return [name];
};

const SustainabilityImpact = () => {
    const [tooltipContent, setTooltipContent] = useState('');

    return (
        <section className="sustainability-impact-section">
            <div className="si-texture-overlay si-top-left"></div>
            <div className="si-texture-overlay si-bottom-right"></div>
            
            <div className="si-wide-container">
                <div className="si-header text-center fade-up" style={{ textAlign: 'center', marginBottom: '60px' }}>
                    <h2 className="si-eyebrow" style={{ justifyContent: 'center' }}>
                        Our Operational Footprint
                    </h2>
                    <div className="si-underline mx-auto" style={{ margin: '15px auto 0' }}></div>
                </div>

                <div className="si-grid" style={{ alignItems: 'center' }}>
                    
                    {/* Left Column: Premium Animated Stats */}
                    <div className="si-stats-panel fade-up" style={{ animationDelay: '0.1s' }}>
                        <div className="si-stats-container">
                            <div className="si-stat-card-premium fade-up" style={{ animationDelay: '0.2s' }}>
                                <div className="si-stat-icon-wrapper"><i className="fas fa-clipboard-check"></i></div>
                                <div className="si-stat-number-premium">
                                    <CountUp end={400000} duration={2.5} separator="," enableScrollSpy scrollSpyOnce />+
                                </div>
                                <div className="si-stat-label-premium">EPR Obligations (MT)</div>
                            </div>
                            
                            <div className="si-stat-card-premium fade-up" style={{ animationDelay: '0.3s' }}>
                                <div className="si-stat-icon-wrapper"><i className="fas fa-truck-pickup"></i></div>
                                <div className="si-stat-number-premium">
                                    <CountUp end={8000} duration={2.5} separator="," enableScrollSpy scrollSpyOnce />+
                                </div>
                                <div className="si-stat-label-premium">Landfill Clearance (MT)</div>
                            </div>

                            <div className="si-stat-card-premium fade-up" style={{ animationDelay: '0.4s' }}>
                                <div className="si-stat-icon-wrapper"><i className="fas fa-recycle"></i></div>
                                <div className="si-stat-number-premium">
                                    <CountUp end={2000} duration={2.5} separator="," enableScrollSpy scrollSpyOnce />+
                                </div>
                                <div className="si-stat-label-premium">Dry Waste Managed (MT)</div>
                            </div>

                            <div className="si-stat-card-premium fade-up" style={{ animationDelay: '0.5s' }}>
                                <div className="si-stat-icon-wrapper"><i className="fas fa-cubes"></i></div>
                                <div className="si-stat-number-premium">
                                    <CountUp end={15000} duration={2.5} separator="," enableScrollSpy scrollSpyOnce />
                                </div>
                                <div className="si-stat-label-premium">Granules Supplied (MT)</div>
                            </div>
                        </div>
                    </div>

                    {/* Right Column: Interactive Map */}
                    <div className="si-map-container fade-up" style={{ animationDelay: '0.3s', position: 'relative' }}>
                    
                    {tooltipContent && (
                        <div className="si-tooltip" style={{
                            position: 'absolute',
                            top: '20px',
                            right: '20px',
                            background: '#fcf9f2',
                            border: '1px solid #dcd5c4',
                            color: '#16261d',
                            padding: '10px 20px',
                            borderRadius: '8px',
                            fontFamily: '"Inter", sans-serif',
                            fontWeight: '600',
                            zIndex: 10,
                            pointerEvents: 'none',
                            boxShadow: '0 10px 25px rgba(0,0,0,0.3)',
                            transition: 'all 0.3s ease'
                        }}>
                            {tooltipContent}
                        </div>
                    )}

                    <ComposableMap
                        projection="geoMercator"
                        projectionConfig={{ scale: 1500, center: [78.0, 22.5] }}
                        className="si-india-map"
                        width={1000}
                        height={900}
                        style={{ filter: 'drop-shadow(0px 20px 40px rgba(0, 0, 0, 0.5))', width: '100%', height: 'auto' }}
                    >
                        <Geographies geography={geoUrl}>
                            {({ geographies }) =>
                                geographies.map((geo) => {
                                    const centroid = geoCentroid(geo);
                                    const stateName = geo.properties.NAME_1 || geo.properties.st_nm || geo.properties.name || "";
                                    const isActive = activeStates.includes(stateName);
                                    
                                    // Custom manual offsets for tight states
                                    let markerCentroid = centroid;
                                    if (stateName === "Goa" && centroid) markerCentroid = [centroid[0] - 0.2, centroid[1]];
                                    if (stateName === "Delhi" && centroid) markerCentroid = [centroid[0] + 0.3, centroid[1]];
                                    
                                    return (
                                        <React.Fragment key={geo.rsmKey}>
                                            <Geography
                                                geography={geo}
                                                onMouseEnter={() => setTooltipContent(stateName)}
                                                onMouseLeave={() => setTooltipContent("")}
                                                fill="#fcf9f2"
                                                stroke="#e5dfce"
                                                strokeWidth={1}
                                                style={{
                                                    default: { outline: "none" },
                                                    hover: { 
                                                        fill: "#e5dfce", 
                                                        stroke: "#a4d65e", 
                                                        strokeWidth: 1.5, 
                                                        outline: "none", 
                                                        transition: "all 250ms ease" 
                                                    },
                                                    pressed: { outline: "none" },
                                                }}
                                            />
                                            {/* State Labels */}
                                            {markerCentroid && stateName && isActive && (
                                                <Marker coordinates={markerCentroid}>
                                                    <text
                                                        y="-2"
                                                        fontSize={8}
                                                        textAnchor="middle"
                                                        fill="rgba(22, 38, 29, 0.85)"
                                                        fontFamily="Inter, sans-serif"
                                                        pointerEvents="none"
                                                        style={{ 
                                                            transition: 'all 0.3s ease', 
                                                            opacity: tooltipContent === stateName ? 1 : 0.85, 
                                                            fontWeight: tooltipContent === stateName ? 'bold' : 'normal', 
                                                            fill: tooltipContent === stateName ? '#16261d' : 'rgba(22, 38, 29, 0.85)',
                                                            filter: 'none'
                                                        }}
                                                    >
                                                        {formatStateName(stateName).map((line, idx) => (
                                                            <tspan x="0" dy={idx === 0 ? 0 : 9} key={line}>{line}</tspan>
                                                        ))}
                                                    </text>
                                                </Marker>
                                            )}
                                        </React.Fragment>
                                    );
                                })
                            }
                        </Geographies>

                        {/* Nagpur Headquarters Marker: [79.0882, 21.1458] */}
                        <Marker coordinates={[79.0882, 21.1458]}>
                            <g className="si-nagpur-marker" 
                               onMouseEnter={() => setTooltipContent("Headquarters: Nagpur, Maharashtra")} 
                               onMouseLeave={() => setTooltipContent("")}
                               style={{ cursor: 'pointer' }}
                            >
                                <circle cx={0} cy={0} r={4} fill="#a4d65e" />
                                <circle cx={0} cy={0} r={8} fill="none" stroke="#16261d" strokeWidth={1.5} />
                                <circle cx={0} cy={0} r={16} fill="none" stroke="#a4d65e" strokeWidth={1.5} className="si-pulse" />
                            </g>
                        </Marker>
                    </ComposableMap>
                </div>
                </div> {/* End si-grid */}
            </div>
        </section>
    );
};

export default SustainabilityImpact;
