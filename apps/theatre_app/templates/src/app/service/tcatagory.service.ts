import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class TcatagoryService {
  constructor(private _http: Http) {}

  createTcatagory(tcatagory) {
    return this._http
      .post("/tcatagory", tcatagory)
      .map(data => data.json())
      .toPromise();
  }
  getGradyear(gradyear) {
    return this._http
      .get("/gradyear", gradyear)
      .map(data => data.json())
      .toPromise();
  }
}
