import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class TrankService {
  constructor(private _http: Http) {}

  createTrank(trank) {
    return this._http
      .post("/trank", trank)
      .map(data => data.json())
      .toPromise();
  }
  getTrank(trank) {
    return this._http.get("/trank").map(data => data.json()).toPromise();
  }
}
