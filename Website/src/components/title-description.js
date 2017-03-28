import React, {Component} from 'react'

export default function(props) {
    return (
        <div className={props.tdCN}>
            <h1 className={props.titleCN}>{props.title}</h1>
            <p className={props.descCN}>{props.text}</p>
        </div>
    )
}
