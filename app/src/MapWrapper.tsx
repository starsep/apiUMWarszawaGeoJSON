import React, {FC, useEffect, useState} from "react";
import Map, {Layer, Source, ViewState} from 'react-map-gl';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

function hashString(parameters: Record<string, string>) {
    return Object
        .entries(parameters)
        .map(([key, value]) => `${key}=${value}`)
        .join("&");
}

export const MapWrapper: FC<{source: string | null}> = ({ source }) => {
    const [viewState, setViewState] = useState<Partial<ViewState>>({
        longitude: 21.0058,
        latitude: 52.2317,
        zoom: 12,
    });

    const hashArgs = [(viewState.zoom || 0.0).toFixed(0), (viewState.latitude || 0.0).toFixed(5), (viewState.longitude || 0.0).toFixed(5)];
    useEffect(() => {
        const [zoom, latitude, longitude] = hashArgs;
        try {
            window.location.hash = hashString({map: `${zoom}/${latitude}/${longitude}`});
        } catch (e: any) {
            console.error(e);
        }
    }, hashArgs);
    return (
        <Map
            mapLib={maplibregl}
            {...viewState}
            onMove={evt => setViewState(evt.viewState)}
            id="map"
            style={{height: "calc(100vh - 50px)", width: "calc(100% - 300px)"}}
            mapStyle="https://api.maptiler.com/maps/openstreetmap/style.json?key=M3LpwRbgQHYmHP1G9rfX"
        >
            {source && <Source id="source" type="geojson" data={`https://umwarszawa.starsep.com/${source}.geojson`}>
                <Layer id="source" type="circle" paint={{ "circle-radius": 10, "circle-color": "red" }} />
            </Source>}
        </Map>
    );
};
