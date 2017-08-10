import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class ThonorService {
  constructor(private _http: Http) {}

  createThonor(thonor) {
    return this._http
      .post("/thonor", thonor)
      .map(data => data.json())
      .toPromise();
  }
  getThonor(thonor) {
    return this._http.get("/thonor").map(data => data.json()).toPromise();
  }
}
