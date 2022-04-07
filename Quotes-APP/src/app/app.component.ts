import { Component } from '@angular/core';
import { Quotes } from './quotes';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  quotes :Quotes[] =[
    {id:1, name: 'You may not control all the events that happen to you, but you can decide not to be reduced by them.'},
    {id:2, name: 'You may not control all the events that happen to you, but you can decide not to be reduced by them.'},
    {id:3, name: 'You may not control all the events that happen to you, but you can decide not to be reduced by them.'},
    {id:4, name: 'You may not control all the events that happen to you, but you can decide not to be reduced by them.'},
    {id:5, name: 'You may not control all the events that happen to you, but you can decide not to be reduced by them.'},
    {id:6, name: 'You may not control all the events that happen to you, but you can decide not to be reduced by them.'},
  ]
  
}
