import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class TpositionService {
  constructor(private _http: Http) {}

  createTposition(tposition) {
    return this._http
      .post("/tposition", tposition)
      .map(data => data.json())
      .toPromise();
  }
  getTposition(tposition) {
    return this._http
      .get("/tposition", tposition)
      .map(data => data.json())
      .toPromise();
  }
}
