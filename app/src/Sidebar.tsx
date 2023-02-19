import React, {FC} from "react";

export const Sidebar: FC<{source: string | null, setSource: (source: string | null) => void}> = ({ source, setSource }) => {
    const layers = [
        ["AED", "aed"],
        ["ATM (Euronet)", "atmEuronet"],
        ["Bicycle Station", "bicycleStation"],
        ["Dormitory", "dormitory"],
        ["Government Office", "governmentOffice"],
        ["Hotel", "hotel"],
        ["Parking P+R", "parkingParkAndRide"],
        ["Pharmacy", "pharmacy"],
        ["Police", "police"],
        ["Public Transport Stops", "publicTransportStops"],
        ["Subway Entrance", "subwayEntrance"],
        ["Theater", "theater"],
    ]
    return (
        <div id="sidebar">
            { layers.map(([label, layer]) => (
                <React.Fragment key={layer}>
                    <label><input type="radio" name="layer" onClick={() => setSource(layer)} checked={layer == source}/>
                        {label}
                        &nbsp;
                        <a href={`https://umwarszawa.starsep.com/${layer}.geojson`} download target="_blank">↓</a>
                    </label>
                </React.Fragment>
            ))}
        </div>
    )
}