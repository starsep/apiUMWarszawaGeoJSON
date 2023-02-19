import React, {useState} from "react";
import {Sidebar} from "./Sidebar";
import {MapWrapper} from "./MapWrapper";


export const Root = () => {
    const [source, setSource] = useState<string | null>(null);
    return (<>
        <nav>
            <a href="/">Home</a>
        </nav>
        <div id="row">
            <Sidebar source={source} setSource={setSource}/>
            <MapWrapper source={source}/>
        </div>
    </>);
}