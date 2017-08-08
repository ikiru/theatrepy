import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class DistrictService {
  constructor(private _http: Http) {}

  createDistrict(district) {
    return this._http
      .post("/district", district)
      .map(data => data.json())
      .toPromise();
  }
  getDistrict(district) {
    return this._http
      .get("/district", district)
      .map(data => data.json())
      .toPromise();
  }
  updateDistrict(district) {
    return this._http
      .patch(`/districts/${district._id}`, district)
      .map(data => data.json())
      .toPromise();
  }

  destroyDistrict(id: string) {
    return this._http
      .delete(`/districts/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
