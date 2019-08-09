import { LoginService } from './login.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'accounting-app';

  constructor(private loginService: LoginService)
  {}
  
}
