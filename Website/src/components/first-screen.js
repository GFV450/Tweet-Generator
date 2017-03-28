import React, {Component} from 'react'
import TitleDescription from './title-description'

export default function(props) {
    const title = "LORD OF THE RINGS TWEET GENERATOR"
    const text = "This will generate tweets based on the text found on the Lord of the Rings books"
    return (
        <div className="firstScreen">
            <TitleDescription tdCN="projectTD" titleCN="projectTitle" descCN ="projectDesc" title={title} text={text} />
        </div>
    )
}
