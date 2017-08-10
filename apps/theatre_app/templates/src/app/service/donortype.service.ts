import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class DonortypeService {
  constructor(private _http: Http) {}

  createDonortype(donortype) {
    return this._http
      .post("/donortype", donortype)
      .map(data => data.json())
      .toPromise();
  }
  getDonortype(donortype) {
    return this._http.get("/donortype").map(data => data.json()).toPromise();
  }
  updateDonor(donortype) {
    return this._http
      .patch(`/donortype/${donortype._id}`, donortype)
      .map(data => data.json())
      .toPromise();
  }

  destroyDonortype(id: string) {
    return this._http
      .delete(`/donortype/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
