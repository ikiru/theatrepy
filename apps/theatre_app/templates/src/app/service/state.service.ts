import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class StateService {
  constructor(private _http: Http) {}

  createStates(state) {
    return this._http
      .post("/state", state)
      .map(data => data.json())
      .toPromise();
  }
  getStates(state) {
    return this._http.get("/state").map(data => data.json()).toPromise();
  }
}
