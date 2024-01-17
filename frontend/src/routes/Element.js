import React from 'react'
import Home from '../pages/Home'
import About from '../pages/About'
import SignUp from '../pages/SignUp'
import ListingDetail from '../pages/ListingDetail'
import Listings from '../pages/Listings'
import LogIn from '../pages/LogIn'
import Notfound from '../pages/Notfound'
import { useRoutes } from "react-router-dom";




const Element = () => {
    const routes = useRoutes([
        {
            path: "/",
            element: <Home/>
        },
        {
            path: "about",
            element: <About/>
        },
        {
            path: "login",
            element: <LogIn/>
        },
        {
            path: "signup",
            element: <SignUp/>
        },
        {
            path: "listings",
            element: <Listings/>
        },
        {
            path: "listingDetail",
            element: <ListingDetail/>
        },
        {
            path: "*",
            element: <Notfound/>
        },
    ])

  return routes
}

export default Element