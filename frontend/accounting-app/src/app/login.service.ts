import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  private username: string = 'alkeshkansal';
  private password: string = 'password';
  private isAuthorized = true;

  login(username:string, password:string)
  {
    if(username == this.username && password == this.password)
    {
      this.isAuthorized = true;
    }
  }

  isAuthenticated()
  {
    return this.isAuthorized;
  }
}
