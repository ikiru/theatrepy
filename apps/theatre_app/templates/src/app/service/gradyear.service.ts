import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class GradyearService {
  constructor(private _http: Http) {}

  createGradyear(gradyear) {
    return this._http
      .post("/gradyear", gradyear)
      .map(data => data.json())
      .toPromise();
  }
  getGradyear(gradyear) {
    return this._http.get("/gradyear").map(data => data.json()).toPromise();
  }
}
