import React from 'react';

import TopBar from './components/topbar/TopBar';
import SideBar from './components/sidebar/SideBar';


const Frame = (props: any) => {
    return (
        <div className="Frame">
            <TopBar />
            <SideBar />
        </div>
    );
}

export default Frame;
