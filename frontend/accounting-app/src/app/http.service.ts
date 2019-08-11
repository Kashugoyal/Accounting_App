import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

import { User } from './app-classes'

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private htpp:HttpClient)
  {

  }

  private getUsersUrl='http://127.0.0.1:5000/get_users';

  get_users()
  {
    let headers = new HttpHeaders({
       'Content-Type': 'application/json',
        'Access-Control-Allow-Origin':'*'});
    return this.htpp.get(this.getUsersUrl, {headers});
  }

}
